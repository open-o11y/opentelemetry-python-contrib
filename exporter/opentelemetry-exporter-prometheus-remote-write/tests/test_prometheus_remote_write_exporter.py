# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from unittest import mock

from opentelemetry.exporter.prometheus_remote_write import (
    Config,
    PrometheusRemoteWriteMetricsExporter,
)
from opentelemetry.exporter.prometheus_remote_write.prom_pb.types_pb2 import (
    Label,
    Sample,
    TimeSeries,
)
from opentelemetry.sdk.metrics import Counter
from opentelemetry.sdk.metrics.export import MetricRecord
from opentelemetry.sdk.metrics.export.aggregate import (
    HistogramAggregator,
    LastValueAggregator,
    MinMaxSumCountAggregator,
    SumAggregator,
    ValueObserverAggregator,
)
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.util import get_dict_as_key


class TestPrometheusRemoteWriteMetricExporter(unittest.TestCase):
    # Initializes test data that is reused across tests
    def setUp(self):
        self._test_config = Config(endpoint="/prom/test_endpoint")
        self._test_metric = Counter(
            "testname", "testdesc", "testunit", int, None
        )

        def generate_record(agg_type):
            return MetricRecord(
                self._test_metric,
                None,
                agg_type(),
                Resource({}),
            )

        self._generate_record = generate_record

        def converter_method(record, name, value):
            return (type(record.aggregator), name, value)

        self._converter_mock = mock.MagicMock(return_value=converter_method)

    # # Ensures export is successful with valid metric_records and config
    # def test_export(self):
    #     record = MetricRecord(
    #         self._test_metric,
    #         self._labels_key,
    #         SumAggregator(),
    #         get_meter_provider().resource,
    #     )
    #     exporter = PrometheusRemoteWriteMetricsExporter(self._test_config)
    #     result = exporter.export([record])
    #     self.assertIs(result, MetricsExportResult.SUCCESS)

    # Ensures conversion to timeseries function as expected for different aggregation types
    def test_convert_to_timeseries(self):
        timeseries_mock_method = mock.Mock(return_value=["test_value"])
        exporter = PrometheusRemoteWriteMetricsExporter(self._test_config)
        exporter.convert_from_sum = timeseries_mock_method
        exporter.convert_from_min_max_sum_count = timeseries_mock_method
        exporter.convert_from_histogram = timeseries_mock_method
        exporter.convert_from_last_value = timeseries_mock_method
        exporter.convert_from_value_observer = timeseries_mock_method
        test_records = [
            self._generate_record(SumAggregator),
            self._generate_record(MinMaxSumCountAggregator),
            self._generate_record(HistogramAggregator),
            self._generate_record(LastValueAggregator),
            self._generate_record(ValueObserverAggregator),
        ]
        data = exporter.convert_to_timeseries(test_records)
        self.assertEqual(len(data), 5)
        for timeseries in data:
            self.assertEqual(timeseries, "test_value")

        no_type_records = [self._generate_record(lambda: None)]
        with self.assertRaises(ValueError):
            exporter.convert_to_timeseries(no_type_records)

    # Ensures sum aggregator is correctly converted to timeseries
    def test_convert_from_sum(self):
        sum_record = self._generate_record(SumAggregator)
        sum_record.aggregator.update(3)
        sum_record.aggregator.update(2)
        sum_record.aggregator.take_checkpoint()

        exporter = PrometheusRemoteWriteMetricsExporter(self._test_config)
        exporter.create_timeseries = self._converter_mock()
        timeseries = exporter.convert_from_sum(sum_record)
        self.assertEqual(timeseries[0], (SumAggregator, "testname", 5))

    # Ensures sum min_max_count aggregator is correctly converted to timeseries
    def test_convert_from_min_max_sum_count(self):
        min_max_sum_count_record = self._generate_record(
            MinMaxSumCountAggregator
        )
        min_max_sum_count_record.aggregator.update(5)
        min_max_sum_count_record.aggregator.update(1)
        min_max_sum_count_record.aggregator.take_checkpoint()

        exporter = PrometheusRemoteWriteMetricsExporter(self._test_config)
        exporter.create_timeseries = self._converter_mock()
        timeseries = exporter.convert_from_min_max_sum_count(
            min_max_sum_count_record
        )
        self.assertEqual(
            timeseries[0], (MinMaxSumCountAggregator, "testname_min", 1)
        )
        self.assertEqual(
            timeseries[1], (MinMaxSumCountAggregator, "testname_max", 5)
        )
        self.assertEqual(
            timeseries[2], (MinMaxSumCountAggregator, "testname_sum", 6)
        )
        self.assertEqual(
            timeseries[3], (MinMaxSumCountAggregator, "testname_count", 2)
        )

    # Ensures histogram aggregator is correctly converted to timeseries
    def test_convert_from_histogram(self):
        histogram_record = self._generate_record(
            HistogramAggregator
        )
        histogram_record.aggregator.update(5)
        histogram_record.aggregator.update(2)
        histogram_record.aggregator.update(-1)
        histogram_record.aggregator.take_checkpoint()

        exporter = PrometheusRemoteWriteMetricsExporter(self._test_config)
        exporter.create_timeseries = self._converter_mock()
        timeseries = exporter.convert_from_histogram(histogram_record)
        self.assertEqual(timeseries[0], (HistogramAggregator, 'testname_bucket{le="0"}', 1))
        self.assertEqual(timeseries[1], (HistogramAggregator, 'testname_bucket{le="+Inf"}', 2))
        self.assertEqual(timeseries[2], (HistogramAggregator, "testname_count", 3))

    # Ensures last value aggregator is correctly converted to timeseries
    def test_convert_from_last_value(self):
        last_value_record = self._generate_record(
            LastValueAggregator
        )
        last_value_record.aggregator.update(1)
        last_value_record.aggregator.update(5)
        last_value_record.aggregator.take_checkpoint()

        exporter = PrometheusRemoteWriteMetricsExporter(self._test_config)
        exporter.create_timeseries = self._converter_mock()
        timeseries = exporter.convert_from_last_value(last_value_record)
        self.assertEqual(timeseries[0], (LastValueAggregator, "testname", 5))

    # Ensures value observer aggregator is correctly converted to timeseries
    def test_convert_from_value_observer(self):
        value_observer_record = self._generate_record(
            ValueObserverAggregator
        )
        value_observer_record.aggregator.update(5)
        value_observer_record.aggregator.update(1)
        value_observer_record.aggregator.update(2)
        value_observer_record.aggregator.take_checkpoint()

        exporter = PrometheusRemoteWriteMetricsExporter(self._test_config)
        exporter.create_timeseries = self._converter_mock()
        timeseries = exporter.convert_from_value_observer(
            value_observer_record
        )
        self.assertEqual(
            timeseries[0], (ValueObserverAggregator, "testname_min", 1)
        )
        self.assertEqual(
            timeseries[1], (ValueObserverAggregator, "testname_max", 5)
        )
        self.assertEqual(
            timeseries[2], (ValueObserverAggregator, "testname_sum", 8)
        )
        self.assertEqual(
            timeseries[3], (ValueObserverAggregator, "testname_count", 3)
        )
        self.assertEqual(
            timeseries[4], (ValueObserverAggregator, "testname_last", 2)
        )

    # TODO: Implement summary converter test once quantile/summary support added to SDK
    def test_convert_from_summary(self):
        pass

    # Ensures timeseries produced contains appropriate sample and labels
    def test_create_timeseries(self):
        sum_aggregator = SumAggregator()
        sum_aggregator.update(5)
        sum_aggregator.take_checkpoint()
        sum_aggregator.last_update_timestamp = 10
        metric_record = MetricRecord(
            self._test_metric,
            get_dict_as_key({"record_name": "record_value"}),
            sum_aggregator,
            Resource({"resource_name": "resource_value"}),
        )
        exporter = PrometheusRemoteWriteMetricsExporter(self._test_config)
        expected_timeseries = TimeSeries()
        expected_timeseries.labels.append(exporter.create_label("__name__", "testname"))
        expected_timeseries.labels.append(exporter.create_label("resource_name", "resource_value"))
        expected_timeseries.labels.append(exporter.create_label("record_name", "record_value"))
        expected_timeseries.samples.append(exporter.create_sample(10, 5.0))
        timeseries = exporter.create_timeseries(metric_record, "testname", 5.0)

    # # Verifies that build_message calls snappy.compress and returns SerializedString
    # @mock.patch("snappy.compress", return_value=1)
    # def test_build_message(self, mock_compress):
    #     data = [
    #         TimeSeriesData(["test_label0"], [0]),
    #         TimeSeriesData(["test_label1"], [1]),
    #     ]
    #     exporter = PrometheusRemoteWriteMetricsExporter(self._test_config)
    #     message = exporter.build_message(data)
    #     self.assertEqual(mock_compress.call_count, 1)
    #     self.assertIsInstance(message, str)

    # # Ensure correct headers are added when valid config is provided
    # def test_get_headers(self):
    #     test_config = self._test_config
    #     test_config["headers"] = {"Custom Header": "test_header"}
    #     test_config["bearer_token"] = "test_token"
    #     exporter = PrometheusRemoteWriteMetricsExporter(test_config)
    #     headers = exporter.get_headers()
    #     self.assertEqual(headers["Content-Encoding"], "snappy")
    #     self.assertEqual(headers["Content-Type"], "application/x-protobuf")
    #     self.assertEqual(headers["X-Prometheus-Remote-Write-Version"], "0.1.0")
    #     self.assertEqual(headers["Authorization"], "test_token")
    #     self.assertEqual(headers["Custom Header"], "test_header")

    # def test_send_request(self):
    #     # TODO: Iron out details of test after implementation
    #     pass

    # # Ensures non alphanumberic label characters gets replaced with underscore
    # def test_sanitize_label(self):
    #     unsanitized_string = "key/metric@data"
    #     exporter = PrometheusRemoteWriteMetricsExporter(self._test_config)
    #     sanitized_string = exporter.sanitize_label(unsanitized_string)
    #     self.assertEqual(sanitized_string, "key_metric_data")

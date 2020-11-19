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
    PrometheusRemoteWriteMetricsExporter,
)
from opentelemetry.exporter.prometheus_remote_write.gen.types_pb2 import (
    TimeSeries,
)
from opentelemetry.sdk.metrics import Counter
from opentelemetry.sdk.metrics.export import ExportRecord, MetricsExportResult
from opentelemetry.sdk.metrics.export.aggregate import (
    HistogramAggregator,
    LastValueAggregator,
    MinMaxSumCountAggregator,
    SumAggregator,
    ValueObserverAggregator,
)
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.util import get_dict_as_key


class TestValidation(unittest.TestCase):
    # Test cases to ensure exporter parameter validation works as intended
    def test_valid_standard_param(self):
        try:
            PrometheusRemoteWriteMetricsExporter(
                endpoint="/prom/test_endpoint",
            )
        except ValueError:
            self.fail("failed to instantiate exporter with valid params)")

    def test_valid_basic_auth_param(self):
        try:
            PrometheusRemoteWriteMetricsExporter(
                endpoint="/prom/test_endpoint",
                basic_auth={
                    "username": "test_username",
                    "password": "test_password",
                },
            )
        except ValueError:
            self.fail("failed to instantiate exporter with valid params)")

    def test_valid_bearer_token_param(self):
        try:
            PrometheusRemoteWriteMetricsExporter(
                endpoint="/prom/test_endpoint",
                bearer_token="test_bearer_token",
            )
        except ValueError:
            self.fail("failed to instantiate exporter with valid params)")

    def test_invalid_no_endpoint_param(self):
        with self.assertRaises(ValueError):
            PrometheusRemoteWriteMetricsExporter("")

    def test_invalid_no_username_param(self):
        with self.assertRaises(ValueError):
            PrometheusRemoteWriteMetricsExporter(
                endpoint="/prom/test_endpoint",
                basic_auth={"password": "test_password"},
            )

    def test_invalid_no_password_param(self):
        with self.assertRaises(ValueError):
            PrometheusRemoteWriteMetricsExporter(
                endpoint="/prom/test_endpoint",
                basic_auth={"username": "test_username"},
            )

    def test_invalid_conflicting_passwords_param(self):
        with self.assertRaises(ValueError):
            PrometheusRemoteWriteMetricsExporter(
                endpoint="/prom/test_endpoint",
                basic_auth={
                    "username": "test_username",
                    "password": "test_password",
                    "password_file": "test_file",
                },
            )

    def test_invalid_conflicting_bearer_tokens_param(self):
        with self.assertRaises(ValueError):
            PrometheusRemoteWriteMetricsExporter(
                endpoint="/prom/test_endpoint",
                bearer_token="test_bearer_token",
                bearer_token_file="test_file",
            )

    def test_invalid_conflicting_auth_param(self):
        with self.assertRaises(ValueError):
            PrometheusRemoteWriteMetricsExporter(
                endpoint="/prom/test_endpoint",
                basic_auth={
                    "username": "test_username",
                    "password": "test_password",
                },
                bearer_token="test_bearer_token",
            )


class TestConversion(unittest.TestCase):
    # Initializes test data that is reused across tests
    def setUp(self):
        self._test_metric = Counter(
            "testname", "testdesc", "testunit", int, None
        )
        self._exporter = PrometheusRemoteWriteMetricsExporter(
            endpoint="/prom/test_endpoint"
        )

        def generate_record(aggregator_type):
            return ExportRecord(
                self._test_metric,
                None,
                aggregator_type(),
                Resource({}),
            )

        self._generate_record = generate_record

        def converter_method(record, name, value):
            return (type(record.aggregator), name, value)

        self._converter_mock = mock.MagicMock(return_value=converter_method)

    # Ensures conversion to timeseries function works with valid aggregation types
    def test_valid_convert_to_timeseries(self):
        timeseries_mock_method = mock.Mock(return_value=["test_value"])
        self._exporter.convert_from_sum = timeseries_mock_method
        self._exporter.convert_from_min_max_sum_count = timeseries_mock_method
        self._exporter.convert_from_histogram = timeseries_mock_method
        self._exporter.convert_from_last_value = timeseries_mock_method
        self._exporter.convert_from_value_observer = timeseries_mock_method
        test_records = [
            self._generate_record(SumAggregator),
            self._generate_record(MinMaxSumCountAggregator),
            self._generate_record(HistogramAggregator),
            self._generate_record(LastValueAggregator),
            self._generate_record(ValueObserverAggregator),
        ]
        data = self._exporter.convert_to_timeseries(test_records)
        self.assertEqual(len(data), 5)
        for timeseries in data:
            self.assertEqual(timeseries, "test_value")

        no_type_records = [self._generate_record(lambda: None)]
        with self.assertRaises(ValueError):
            self._exporter.convert_to_timeseries(no_type_records)

    # Ensures conversion to timeseries fails for unsupported aggregation types
    def test_invalid_convert_to_timeseries(self):
        no_type_records = [self._generate_record(lambda: None)]
        with self.assertRaises(ValueError):
            self._exporter.convert_to_timeseries(no_type_records)

    # Ensures sum aggregator is correctly converted to timeseries
    def test_convert_from_sum(self):
        sum_record = self._generate_record(SumAggregator)
        sum_record.aggregator.update(3)
        sum_record.aggregator.update(2)
        sum_record.aggregator.take_checkpoint()

        self._exporter.create_timeseries = self._converter_mock()
        timeseries = self._exporter.convert_from_sum(sum_record)
        self.assertEqual(timeseries[0], (SumAggregator, "testname", 5))

    # Ensures sum min_max_count aggregator is correctly converted to timeseries
    def test_convert_from_min_max_sum_count(self):
        min_max_sum_count_record = self._generate_record(
            MinMaxSumCountAggregator
        )
        min_max_sum_count_record.aggregator.update(5)
        min_max_sum_count_record.aggregator.update(1)
        min_max_sum_count_record.aggregator.take_checkpoint()

        self._exporter.create_timeseries = self._converter_mock()
        timeseries = self._exporter.convert_from_min_max_sum_count(
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
        histogram_record = self._generate_record(HistogramAggregator)
        histogram_record.aggregator.update(5)
        histogram_record.aggregator.update(2)
        histogram_record.aggregator.update(-1)
        histogram_record.aggregator.take_checkpoint()

        self._exporter.create_timeseries = self._converter_mock()
        timeseries = self._exporter.convert_from_histogram(histogram_record)
        self.assertEqual(
            timeseries[0], (HistogramAggregator, 'testname_bucket{le="0"}', 1)
        )
        self.assertEqual(
            timeseries[1],
            (HistogramAggregator, 'testname_bucket{le="+Inf"}', 2),
        )
        self.assertEqual(
            timeseries[2], (HistogramAggregator, "testname_count", 3)
        )

    # Ensures last value aggregator is correctly converted to timeseries
    def test_convert_from_last_value(self):
        last_value_record = self._generate_record(LastValueAggregator)
        last_value_record.aggregator.update(1)
        last_value_record.aggregator.update(5)
        last_value_record.aggregator.take_checkpoint()

        self._exporter.create_timeseries = self._converter_mock()
        timeseries = self._exporter.convert_from_last_value(last_value_record)
        self.assertEqual(timeseries[0], (LastValueAggregator, "testname", 5))

    # Ensures value observer aggregator is correctly converted to timeseries
    def test_convert_from_value_observer(self):
        value_observer_record = self._generate_record(ValueObserverAggregator)
        value_observer_record.aggregator.update(5)
        value_observer_record.aggregator.update(1)
        value_observer_record.aggregator.update(2)
        value_observer_record.aggregator.take_checkpoint()

        self._exporter.create_timeseries = self._converter_mock()
        timeseries = self._exporter.convert_from_value_observer(
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

    # Ensures quantile aggregator is correctly converted to timeseries
    # TODO: Add test once method is implemented
    def test_convert_from_quantile(self):
        pass

    # Ensures timeseries produced contains appropriate sample and labels
    def test_create_timeseries(self):
        sum_aggregator = SumAggregator()
        sum_aggregator.update(5)
        sum_aggregator.take_checkpoint()
        sum_aggregator.last_update_timestamp = 10
        export_record = ExportRecord(
            self._test_metric,
            get_dict_as_key({"record_name": "record_value"}),
            sum_aggregator,
            Resource({"resource_name": "resource_value"}),
        )

        expected_timeseries = TimeSeries()
        expected_timeseries.labels.append(
            self._exporter.create_label("__name__", "testname")
        )
        expected_timeseries.labels.append(
            self._exporter.create_label("resource_name", "resource_value")
        )
        expected_timeseries.labels.append(
            self._exporter.create_label("record_name", "record_value")
        )
        expected_timeseries.samples.append(
            self._exporter.create_sample(10, 5.0),
        )
        timeseries = self._exporter.create_timeseries(
            export_record, "testname", 5.0,
        )
        self.assertEqual(timeseries, expected_timeseries)

    # Ensure correct headers are added when valid config is provided
    def test_get_headers(self):
        self._exporter.headers = {"Custom Header": "test_header"}
        self._exporter.headers = {"Custom Header": "test_header"}
        self._exporter.bearer_token = "test_token"

        headers = self._exporter.get_headers()
        self.assertEqual(headers.get("Content-Encoding", ""), "snappy")
        self.assertEqual(
            headers.get("Content-Type", ""), "application/x-protobuf"
        )
        self.assertEqual(
            headers.get("X-Prometheus-Remote-Write-Version", ""), "0.1.0"
        )
        self.assertEqual(headers.get("Authorization", ""), "Bearer test_token")
        self.assertEqual(headers.get("Custom Header", ""), "test_header")


class ResponseStub:
    def __init__(self, status_code):
        self.status_code = status_code
        self.reason = "dummy_reason"
        self.content = "dummy_content"


class TestExport(unittest.TestCase):
    def setUp(self):
        self._exporter = PrometheusRemoteWriteMetricsExporter(
            endpoint="/prom/test_endpoint"
        )

    # Ensures export is successful with valid export_records and config
    def test_export(self):
        record = ExportRecord(
            self._test_metric,
            None,
            SumAggregator(),
            Resource({}),
        )
        self._exporter.convert_to_timeseries = mock.Mock(return_value=[])
        self._exporter.build_message = mock.Mock(return_value=bytes())
        self._exporter.get_headers = mock.Mock(return_value={})
        self._exporter.send_message = mock.Mock(
            return_value=MetricsExportResult.SUCCESS
        )
        result = self._exporter.export([record])
        self.assertIs(result, MetricsExportResult.SUCCESS)

    @mock.patch("requests.post", return_value=ResponseStub(200))
    def test_valid_send_message(self, mock_post):
        result = self._exporter.send_message(bytes(), {})
        self.assertEqual(mock_post.call_count, 1)
        self.assertEqual(result, MetricsExportResult.SUCCESS)

    @mock.patch("requests.post", return_value=ResponseStub(404))
    def test_invalid_send_message(self, mock_post):
        result = self._exporter.send_message(bytes(), {})
        self.assertEqual(mock_post.call_count, 1)
        self.assertEqual(result, MetricsExportResult.FAILURE)

    # Verifies that build_message calls snappy.compress and returns SerializedString
    @mock.patch("snappy.compress", return_value=bytes())
    def test_build_message(self, mock_compress):
        test_timeseries = [
            TimeSeries(),
            TimeSeries(),
        ]
        message = self._exporter.build_message(test_timeseries)
        self.assertEqual(mock_compress.call_count, 1)
        self.assertIsInstance(message, bytes)

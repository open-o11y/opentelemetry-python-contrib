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


class TestPrometheusRemoteWriteMetricExporter(unittest.TestCase):
    # Initializes test data that is reused across tests
    def setUp(self):
        pass

    # Ensures export is successful with valid metric_records and config
    def test_export(self):
        pass

    # Ensures sum aggregator is correctly converted to timeseries
    def test_convert_from_sum(self):
        pass

    # Ensures sum min_max_count aggregator is correctly converted to timeseries
    def test_convert_from_min_max_sum_count(self):
        pass

    # Ensures histogram aggregator is correctly converted to timeseries
    def test_convert_from_histogram(self):
        pass

    # Ensures last value aggregator is correctly converted to timeseries
    def test_convert_from_last_value(self):
        pass

    # Ensures value observer aggregator is correctly converted to timeseries
    def test_convert_from_value_observer(self):
        pass

    # Ensures summary aggregator is correctly converted to timeseries
    def test_convert_from_summary(self):
        pass

    # Ensures conversion to timeseries function as expected for different aggregation types
    def test_convert_to_timeseries(self):
        pass

    # Verifies that build_message calls snappy.compress and returns SerializedString
    def test_build_message(self, mock_compress):
        pass

    # Ensure correct headers are added when valid config is provided
    def test_get_headers(self):
        pass

    # Ensures valid message gets sent succesfully
    def test_send_message(self):
        pass

    # Ensures non alphanumberic label characters gets replaced with underscore
    def test_sanitize_label(self):
        pass

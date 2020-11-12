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


from typing import Dict, Sequence

from opentelemetry.sdk.metrics.export import (
    MetricRecord,
    MetricsExporter,
    MetricsExportResult,
)


class TimeSeries:
    """
    TimeSeries class used to store timeseries labels and samples that need to be sent
    Args:
        labels: timeseries labels
        samples: timeseries samples
    """

    def __init__(self):
        pass


class Config:
    """
    Configuration containing all necessary information to make remote write requests

    Args:
        endpoint: url where data will be sent
        basic_auth: username and password for authentication (Optional)
        bearer_token: token used for authentication (Optional)
        bearer_token_file: filepath to file containing authentication token (Optional)
        headers: additional headers for remote write request (Optional)
    """

    def __init__(
        self,
        endpoint: str,
        basic_auth: Dict = None,
        bearer_token: str = None,
        bearer_token_file: str = None,
        headers: Dict = None,
    ):
        pass

    def validate(self):
        pass


class PrometheusRemoteWriteMetricsExporter(MetricsExporter):
    """
    Prometheus remote write metric exporter for OpenTelemetry.

    Args:
        config: configuration containing all necessary information to make remote write requests
    """

    def __init__(self, config: Config):
        pass

    def export(
        self, metric_records: Sequence[MetricRecord]
    ) -> MetricsExportResult:
        pass

    def shutdown(self) -> None:
        pass

    def convert_to_timeseries(
        self, metric_records: Sequence[MetricRecord]
    ) -> Sequence[TimeSeries]:
        pass

    def convert_from_sum(self, sum_record: MetricRecord) -> TimeSeries:
        pass

    def convert_from_min_max_sum_count(
        self, min_max_sum_count_record: MetricRecord
    ) -> TimeSeries:
        pass

    def convert_from_histogram(
        self, histogram_record: MetricRecord
    ) -> TimeSeries:
        pass

    def convert_from_last_value(
        self, last_value_record: MetricRecord
    ) -> TimeSeries:
        pass

    def convert_from_value_observer(
        self, value_observer_record: MetricRecord
    ) -> TimeSeries:
        pass

    def convert_from_summary(self, summary_record: MetricRecord) -> TimeSeries:
        pass

    def sanitize_label(self, label: str) -> str:
        pass

    def build_message(self, data: Sequence[TimeSeries]) -> str:
        pass

    def get_headers(self) -> Dict:
        pass

    def send_message(self, message: str, headers: Dict) -> int:
        pass


def parse_config() -> Config:
    """
    Method that parses yaml file to generate a valid remote write exporter config

    Args:
        path: filepath to yaml configuration file
    """

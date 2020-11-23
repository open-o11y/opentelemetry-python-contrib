from opentelemetry import metrics
from opentelemetry.exporter.prometheus_remote_write import (
    PrometheusRemoteWriteMetricsExporter,
)
from opentelemetry.test.test_base import TestBase


def observer_callback(observer):
    array = [1.0, 15.0, 25.0, 26.0]
    for (index, usage) in enumerate(array):
        labels = {"test_label": str(index)}
        observer.observe(usage, labels)


class TestPrometheusRemoteWriteExporterCortex(TestBase):
    def setUp(self):
        super().setUp
        self.exporter = PrometheusRemoteWriteMetricsExporter(
            endpoint="http://localhost:9009/api/prom/push",
            headers={"X-Scope-Org-ID": "5"},
        )
        self.labels = {"environment": "testing"}
        self.meter = self.meter_provider.get_meter(__name__)
        metrics.get_meter_provider().start_pipeline(
            self.meter, self.exporter, 1,
        )

    def test_export_counter(self):
        requests_counter = self.meter.create_counter(
            name="counter",
            description="test_export_counter",
            unit="1",
            value_type=int,
        )
        requests_counter.add(25, self.labels)

    def test_export_valuerecorder(self):
        requests_size = self.meter.create_valuerecorder(
            name="valuerecorder",
            description="test_export_valuerecorder",
            unit="1",
            value_type=int,
        )
        requests_size.record(25, self.labels)

    def test_export_updowncounter(self):
        requests_size = self.meter.create_updowncounter(
            name="updowncounter",
            description="test_export_updowncounter",
            unit="1",
            value_type=int,
        )
        requests_size.add(-25, self.labels)

    def test_export_sumobserver(self):
        self.meter.register_sumobserver(
            callback=observer_callback,
            name="sumobserver",
            description="test_export_sumobserver",
            unit="1",
            value_type=float,
        )

    def test_export_updownsumobserver(self):
        self.meter.register_updownsumobserver(
            callback=observer_callback,
            name="updownsumobserver",
            description="test_export_updownsumobserver",
            unit="1",
            value_type=float,
        )

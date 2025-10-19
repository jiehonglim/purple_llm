from opentelemetry import metrics
from opentelemetry.exporter.prometheus import PrometheusMetricsExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import Resource

# Initialize the OpenTelemetry metrics
resource = Resource.create({"service.name": "streamlit-llm-otel"})
meter_provider = MeterProvider(resource=resource)
metrics.set_meter_provider(meter_provider)

# Create a Prometheus exporter
exporter = PrometheusMetricsExporter()
reader = PeriodicExportingMetricReader(exporter, export_interval_millis=5000)
meter_provider.start_pipeline(reader)

# Create a meter
meter = metrics.get_meter(__name__)

# Define metrics
request_count = meter.create_counter(
    "request_count",
    description="Counts the number of requests received"
)

response_time = meter.create_histogram(
    "response_time",
    description="Measures the response time of requests"
)

# Functions to record metrics
def record_request():
    request_count.add(1)

def record_response_time(duration):
    response_time.record(duration)
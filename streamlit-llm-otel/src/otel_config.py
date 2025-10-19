from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.metrics import MeterProvider
from opentelemetry.exporter.prometheus import PrometheusMetricsExporter

def setup_tracing():
    resource = Resource.create({"service.name": "streamlit-llm-otel"})
    trace.set_tracer_provider(TracerProvider(resource=resource))
    tracer = trace.get_tracer(__name__)

    otlp_exporter = OTLPSpanExporter()
    span_processor = BatchSpanProcessor(otlp_exporter)
    trace.get_tracer_provider().add_span_processor(span_processor)

    return tracer

def setup_metrics():
    meter_provider = MeterProvider()
    metrics_exporter = PrometheusMetricsExporter()
    meter_provider.start_pipeline(metrics_exporter)

def initialize_observability():
    setup_tracing()
    setup_metrics()
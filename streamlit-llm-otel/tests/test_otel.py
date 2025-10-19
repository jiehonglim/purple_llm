import pytest
from unittest.mock import patch
from src.otel_config import init_tracer, init_metrics
from src.observability.tracer import start_trace, end_trace
from src.observability.metrics import record_metric

@pytest.fixture(scope="module")
def setup_otel():
    init_tracer()
    init_metrics()
    yield
    # Cleanup code if needed

def test_start_trace(setup_otel):
    with patch('src.observability.tracer.tracer.start_span') as mock_start_span:
        start_trace("test_operation")
        mock_start_span.assert_called_once_with("test_operation")

def test_end_trace(setup_otel):
    with patch('src.observability.tracer.tracer.active_span') as mock_active_span:
        mock_active_span = True
        end_trace()
        mock_active_span.end.assert_called_once()

def test_record_metric(setup_otel):
    with patch('src.observability.metrics.metrics_client.record') as mock_record:
        record_metric("test_metric", 1)
        mock_record.assert_called_once_with("test_metric", 1)
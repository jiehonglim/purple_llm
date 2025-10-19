import streamlit as st
from src.llm_client import LLMClient
from src.otel_config import init_otel
from src.observability.tracer import start_trace
from src.observability.metrics import record_metric

# Initialize OpenTelemetry
init_otel()

# Initialize LLM Client
llm_client = LLMClient()

def main():
    st.title("LLM Observability with OpenTelemetry")

    user_input = st.text_input("Enter your query:")
    
    if st.button("Submit"):
        with start_trace("llm_request"):
            response = llm_client.send_request(user_input)
            record_metric("llm_requests", 1)
            st.write("Response from LLM:", response)

if __name__ == "__main__":
    main()
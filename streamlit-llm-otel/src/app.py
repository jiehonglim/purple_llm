from streamlit import st
from llm_client import LLMClient
from observability.tracer import init_tracer
from observability.metrics import init_metrics

# Initialize OpenTelemetry
tracer = init_tracer()
metrics = init_metrics()

# Initialize LLM Client
llm_client = LLMClient()

def main():
    st.title("LLM Observability with OpenTelemetry")
    
    user_input = st.text_input("Enter your query:")
    
    if st.button("Submit"):
        with tracer.start_as_current_span("llm_request"):
            response = llm_client.send_request(user_input)
            st.write("Response from LLM:", response)
            metrics.record_request(user_input, response)

if __name__ == "__main__":
    main()
from streamlit import st

def display_header():
    st.title("LLM Observability Dashboard")
    st.subheader("Monitor your LLM interactions with OpenTelemetry")

def display_metrics(metrics):
    st.metric(label="Requests Made", value=metrics['requests_made'])
    st.metric(label="Successful Responses", value=metrics['successful_responses'])
    st.metric(label="Error Responses", value=metrics['error_responses'])

def display_form():
    with st.form(key='llm_form'):
        user_input = st.text_area("Enter your query:")
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            st.session_state['user_input'] = user_input
            st.success("Query submitted!")

def display_response(response):
    if response:
        st.text_area("LLM Response:", value=response, height=300)

def render_ui(metrics, response):
    display_header()
    display_metrics(metrics)
    display_form()
    display_response(response)
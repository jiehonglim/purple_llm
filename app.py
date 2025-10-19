import streamlit as st
from openai import OpenAI
from elasticsearch import Elasticsearch
from datetime import datetime, timezone
import uuid

openai_key = st.secrets["openai_api_key"]
es_api_key = st.secrets["elastic_cloud_api_key"]
es_url = st.secrets["elastic_cloud_url"]

# Initialize Elasticsearch
es = Elasticsearch(
    es_url,
    api_key=es_api_key
)


# Initialize session
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

st.title("🤖 AI Assistant - Purple Team Test Environment")

# User input
user_prompt = st.text_area("Enter your prompt:", height=150)

if st.button("Submit"):
    # Get response from LLM (example with OpenAI)
    # OpenAI.api_key = st.secrets["openai_api_key"]

    client_oai = OpenAI(api_key=openai_key)

    try:
        response = client_oai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_prompt}
            ]
        )
        
        llm_response = response.choices[0].message.content
        
        # Display response
        st.success("Response:")
        st.write(llm_response)
        
        # Log to Elasticsearch
        log_document = {
            "@timestamp": datetime.now(timezone.utc).isoformat(),
            "event.category": ["genai"],
            "event.type": ["info"],
            "user.id": st.session_state.get("user_id", "anonymous"),
            "user.name": st.session_state.get("user_name", "Anonymous User"),
            "genai.prompt.text": user_prompt,
            "genai.response.text": llm_response,
            "genai.model.name": "gpt-4",
            "genai.model.provider": "openai",
            "session.id": st.session_state.session_id
        }
        
        # Index with pipeline
        es.index(
            index=f"genai-prompts-{datetime.now(timezone.utc).strftime('%Y.%m.%d')}",
            document=log_document,
            pipeline="genai-prompt-classifier"
        )
        
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Display session info
st.sidebar.write(f"Session ID: {st.session_state.session_id}")
class LLMClient:
    def __init__(self, api_key: str, endpoint: str):
        self.api_key = api_key
        self.endpoint = endpoint

    def send_request(self, prompt: str) -> dict:
        import requests
        from observability.tracer import trace_request

        with trace_request("llm_request"):
            headers = {"Authorization": f"Bearer {self.api_key}"}
            response = requests.post(self.endpoint, json={"prompt": prompt}, headers=headers)
            response.raise_for_status()
            return response.json()

    def get_response(self, prompt: str) -> str:
        response_data = self.send_request(prompt)
        return response_data.get("response", "")
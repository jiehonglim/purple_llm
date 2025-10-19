# Streamlit LLM OpenTelemetry Observability

This project is a Streamlit application that integrates OpenTelemetry for observability, specifically designed for interacting with a Large Language Model (LLM). It provides a user-friendly interface for making requests to the LLM and includes robust monitoring capabilities to track performance and usage metrics.

## Project Structure

```
streamlit-llm-otel
├── src
│   ├── app.py                # Main entry point for the Streamlit application
│   ├── llm_client.py         # Handles interactions with the LLM API
│   ├── otel_config.py        # OpenTelemetry configuration setup
│   ├── observability
│   │   ├── tracer.py         # Functions for creating and managing traces
│   │   └── metrics.py        # Functions for recording and exporting metrics
│   ├── components
│   │   └── ui.py             # UI components for the Streamlit app
│   └── utils
│       └── config.py         # Utility functions for configuration management
├── tests
│   ├── test_app.py           # Unit tests for the main application logic
│   └── test_otel.py          # Unit tests for OpenTelemetry integration
├── .streamlit
│   └── config.toml           # Streamlit application configuration settings
├── docker-compose.yml         # Docker services and configurations
├── otel-collector-config.yml  # OpenTelemetry Collector configuration
├── Dockerfile                 # Instructions for building the Docker image
├── requirements.txt           # Python dependencies for the project
├── pyproject.toml             # Project metadata and dependencies
├── .gitignore                 # Files and directories to ignore by Git
└── README.md                  # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-llm-otel
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the OpenTelemetry Collector by configuring `otel-collector-config.yml` as needed.

## Running the Application

To run the Streamlit application, execute the following command:
```
streamlit run src/app.py
```

## Testing

To run the tests, use:
```
pytest tests/
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
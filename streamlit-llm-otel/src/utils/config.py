from pathlib import Path
import json

def load_config(config_file: str) -> dict:
    config_path = Path(config_file)
    if not config_path.is_file():
        raise FileNotFoundError(f"Configuration file {config_file} not found.")
    
    with open(config_path, 'r') as file:
        return json.load(file)

def save_config(config_file: str, config_data: dict) -> None:
    with open(config_file, 'w') as file:
        json.dump(config_data, file, indent=4)

def get_default_config() -> dict:
    return {
        "llm_api_url": "https://api.example.com/llm",
        "api_key": "your_api_key_here",
        "timeout": 30,
        "tracing_enabled": True,
        "metrics_enabled": True
    }
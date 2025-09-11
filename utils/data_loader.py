# utils/data_loader.py
import json
import os

def load_json(filename: str):
    """
    Load JSON file from test_data folder.
    Usage: data = load_json("login_data.json")
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))  # project root
    file_path = os.path.join(base_dir, "test_data", filename)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Test data file not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_login_scenario(key: str):
    data = load_json("login_data.json")
    if key not in data:
        raise KeyError(f"Scenario '{key}' not found in login_data.json")
    return data[key]

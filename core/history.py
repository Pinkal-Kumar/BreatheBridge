# Example: core/history.py
import json
import os

def save_conversation(state):
    user = state.get("user_name", "unknown")
    session_id = state.get("session_id", "default")
    history_dir = "history"
    os.makedirs(history_dir, exist_ok=True)
    file_path = os.path.join(history_dir, f"{user}_{session_id}.json")
    with open(file_path, "w") as f:
        json.dump(state, f, indent=2)
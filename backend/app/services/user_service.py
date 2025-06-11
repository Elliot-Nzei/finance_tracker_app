import json
from pathlib import Path

DATA_FILE = Path("data/processed/users.json")
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)


def save_user(user_data: dict):
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            users = json.load(f)
    else:
        users = {}

    email = user_data["email"]
    users[email] = user_data

    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=2)


def load_user(email: str) -> dict | None:
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            users = json.load(f)
        return users.get(email)
    return None

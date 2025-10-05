import os
import json

DB_FILE = os.path.join(os.path.dirname(__file__), "db", "payments.json")

def load_payments():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_payments(payments):
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(payments, f, indent=2)

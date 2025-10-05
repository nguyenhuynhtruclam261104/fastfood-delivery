import os
import json

DB_FILE = os.path.join(os.path.dirname(__file__), "db", "orders.json")

def load_orders():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_orders(orders):
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(orders, f, indent=2)

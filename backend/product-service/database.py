import os
import json

DB_FILE = os.path.join(os.path.dirname(__file__), "db", "products.json")

def load_products():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_products(products):
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=2)

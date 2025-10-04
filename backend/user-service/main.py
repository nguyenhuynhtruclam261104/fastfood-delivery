from fastapi import FastAPI
from prometheus_client import start_http_server, Counter, Gauge

app = FastAPI()

orders_created = Counter("orders_created", "Total number of orders")
orders_total = Gauge("orders_total", "Current number of orders")

# Metrics server trên cổng 8001
start_http_server(8001)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/order")
def create_order(item_id: int, quantity: int):
    orders_created.inc(quantity)
    orders_total.inc(quantity)
    return {"message": "Order received", "order": {"item_id": item_id, "quantity": quantity}}

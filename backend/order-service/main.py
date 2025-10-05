from fastapi import FastAPI, HTTPException
from database import load_orders, save_orders

app = FastAPI(title="Order Service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/order")
def create_order(user_id: int, product_ids: str):
    orders = load_orders()
    order_id = len(orders) + 1
    order = {"id": order_id, "user_id": user_id, "product_ids": product_ids, "status": "pending"}
    orders.append(order)
    save_orders(orders)
    return order

@app.get("/order/{order_id}")
def get_order(order_id: int):
    orders = load_orders()
    for o in orders:
        if o["id"] == order_id:
            return o
    raise HTTPException(status_code=404, detail="Not found")

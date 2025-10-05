from fastapi import FastAPI

app = FastAPI()

orders = []

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/order")
def create_order(item_id: int, quantity: int):
    order = {"item_id": item_id, "quantity": quantity}
    orders.append(order)
    return {"message": "Order received", "order": order}

from fastapi import FastAPI, HTTPException
from database import load_payments, save_payments

app = FastAPI(title="Payment Service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/payment")
def create_payment(order_id: int, amount: float):
    payments = load_payments()
    payment_id = len(payments) + 1
    payment = {"id": payment_id, "order_id": order_id, "amount": amount, "status": "paid"}
    payments.append(payment)
    save_payments(payments)
    return payment

@app.get("/payment/{payment_id}")
def get_payment(payment_id: int):
    payments = load_payments()
    for p in payments:
        if p["id"] == payment_id:
            return p
    raise HTTPException(status_code=404, detail="Not found")

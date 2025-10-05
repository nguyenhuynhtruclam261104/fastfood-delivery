from fastapi import FastAPI

app = FastAPI()

payments = []

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/payment")
def create_payment(order_id: int, amount: float):
    payment = {"order_id": order_id, "amount": amount}
    payments.append(payment)
    return {"message": "Payment received", "payment": payment}

@app.get("/payments")
def list_payments():
    return {"payments": payments}

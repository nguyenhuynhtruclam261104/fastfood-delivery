from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/user")
def create_user(name: str, email: str):
    return {"message": "User created", "user": {"name": name, "email": email}}

from fastapi import FastAPI, HTTPException
from database import load_users, save_users

app = FastAPI(title="User Service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/user")
def create_user(username: str, email: str):
    users = load_users()
    user_id = len(users) + 1
    user = {"id": user_id, "username": username, "email": email, "address": "123 ABC Street"}
    users.append(user)
    save_users(users)
    return {"message": "User registered", "user": user}

@app.get("/user/{user_id}/profile")
def get_user_profile(user_id: int):
    users = load_users()
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="Not found")

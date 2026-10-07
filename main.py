from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    email: str
    age: int


users = []


@app.get("/")
def home():
    return {
        "message": "Project 2 Backend API is running"
    }


@app.get("/users")
def get_users():
    return users


@app.post("/users")
def create_user(user: User):
    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email,
        "age": user.age
    }

    users.append(new_user)

    return {
        "message": "User created successfully",
        "user": new_user
    }
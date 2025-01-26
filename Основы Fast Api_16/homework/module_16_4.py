from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
def get_users():
    return users


@app.post("/user/{username}/{age}")
def create_user(username: str, age: int):
    if not username:
        raise HTTPException(status_code=400, detail="Username cannot be empty")

    if age <= 0:
        raise HTTPException(status_code=400, detail="Age must be a positive number")

    user_id = 1 if not users else users[-1].id + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: int, username: str, age: int):
    if not username:
        raise HTTPException(status_code=400, detail="Username cannot be empty")

    if age <= 0:
        raise HTTPException(status_code=400, detail="Age must be a positive number")

    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user

    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(i)
            return deleted_user

    raise HTTPException(status_code=404, detail="User was not found")
from fastapi import FastAPI, Request, Path, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Пример данных пользователей
users = [
    {"id": 1, "username": "UrbanUser", "age": 24},
    {"id": 2, "username": "UrbanTest", "age": 22},
    {"id": 3, "username": "Capybara", "age": 60},
]


# Модель для создания пользователя
class UserCreate(BaseModel):
    username: str
    age: int


# Модель для обновления пользователя
class UserUpdate(BaseModel):
    username: Optional[str] = None
    age: Optional[int] = None


# Главная страница
@app.get("/", response_class=HTMLResponse, summary="Get main page", description="Returns the main page with a list of users.")
async def read_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


# Получить пользователя по ID
@app.get("/user/{user_id}", summary="Get user by ID", description="Returns details of a specific user by their ID.")
async def get_user(user_id: int = Path(..., description="The ID of the user to retrieve")):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


# Удалить пользователя по ID
@app.delete("/user/{user_id}", summary="Delete user by ID", description="Deletes a specific user by their ID.")
async def delete_user(user_id: int = Path(..., description="The ID of the user to delete")):
    global users
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        users = [u for u in users if u["id"] != user_id]
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")


# Создать нового пользователя
@app.post("/user/{username}/{age}", summary="Create a new user", description="Creates a new user with the provided username and age.")
async def create_user(username: str = Path(..., description="The username of the new user"),
                      age: int = Path(..., description="The age of the new user")):
    new_user = {"id": len(users) + 1, "username": username, "age": age}
    users.append(new_user)
    return new_user


# Обновить пользователя по ID
@app.put("/user/{user_id}/{username}/{age}", summary="Update user by ID", description="Updates a specific user by their ID with new username and age.")
async def update_user(user_id: int = Path(..., description="The ID of the user to update"),
                      username: str = Path(..., description="The new username"),
                      age: int = Path(..., description="The new age")):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        user["username"] = username
        user["age"] = age
        return user
    raise HTTPException(status_code=404, detail="User not found")
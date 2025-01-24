from fastapi import FastAPI

app = FastAPI()


# Маршрут для главной страницы
@app.get("/")
def get_main_page():
    return {"message": "Главная страница"}


# Маршрут для страницы администратора
@app.get("/user/admin")
def get_admin_page():
    return {"message": "Вы вошли как администратор"}


# Маршрут для страницы пользователя с параметром в пути
@app.get("/user/{user_id}")
def get_user_by_id(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


# Маршрут для страницы пользователя с параметрами в адресной строке
@app.get("/user")
def get_user_info(username: str, age: int):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
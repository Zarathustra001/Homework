from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/user/{user_id}")
def get_user_by_id(
    user_id: Annotated[
        int,
        Path(
            title="User ID",
            description="Enter User ID",
            ge=1,
            le=100,
            example=1,
        ),
    ]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/{age}")
def get_user_info(
    username: Annotated[
        str,
        Path(
            title="Username",
            description="Enter username",
            min_length=5,
            max_length=20,
            example="UrbanUser",
        ),
    ],
    age: Annotated[
        int,
        Path(
            title="Age",
            description="Enter age",
            ge=18,
            le=120,
            example=24,
        ),
    ],
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
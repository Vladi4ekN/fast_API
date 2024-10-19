from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# Главная страница
@app.get("/main")
async def read_root():
    return {"message": "Главная страница"}

# Страница администратора
@app.get("/user/admin")
async def read_admin():
    return {"message": "Вы вошли как администратор"}

# Страница пользователя с параметром в пути
@app.get("/user/{user_id}")
async def read_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Страница пользователя с параметрами в адресной строке
@app.get("/user")
async def read_user_info(username: str, age: int):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

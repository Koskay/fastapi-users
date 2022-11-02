from asyncpg import UniqueViolationError
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from ormar import NoMatch

from .models import Person
from .schemas import UserAuth
from .services import validate_birthday

router = APIRouter()


@router.post("/auth/register", status_code=201)
async def create_item(person: Person):
    if not await validate_birthday(person):
        return JSONResponse(status_code=422, content={"422": "Регистрация доступна только лицам 18+"})
    try:
        await person.save()  # сохранение пользователя в бд
        return {'id': person.id}
    except UniqueViolationError:  # ловим исключение если пользователь с таким логином уже есть в базе
        raise HTTPException(status_code=400, detail='Пользователь с таким логином уже существует')


@router.get("/user/{pk}", status_code=200, response_model=Person, response_model_exclude={'password'})
async def read_item(pk: int):
    try:
        return await Person.objects.get(pk=pk)
    except NoMatch:  # ловим исключение если пользавателя нет в бд
        return JSONResponse(status_code=404, content={"404": "Такой пользователь не зарегестрирован"})


@router.post("/auth/login", status_code=200)
async def create_aa(user_auth: UserAuth):
    try:
        user = await Person.objects.get(**user_auth.dict())
        return {"id": user.id}
    except NoMatch:
        return JSONResponse(status_code=404, content={"404": "Такой пользователь не зарегестрирован,"
                                                      "Либо вы ввели неверный логин или пароль"})
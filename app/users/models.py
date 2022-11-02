import datetime
import ormar

from database.db_connect import metadata, conn


class Person(ormar.Model):
    """Модель пользователя"""

    class Meta:
        metadata = metadata
        database = conn

    id: int = ormar.Integer(primary_key=True)
    phone: str = ormar.String(max_length=50)
    login: str = ormar.String(max_length=100, unique=True)
    password: str = ormar.String(max_length=100)
    name: str = ormar.String(max_length=50)
    birth: datetime.date = ormar.Date()
    tg: str = ormar.String(max_length=100, nullable=True)
    email: str = ormar.String(max_length=200, nullable=True)
    # @validator('birth')
    # def check_birth(cls, v):
    #     user_old = datetime.date.today() - v
    #     days_at_eighteen = 6574
    #     if user_old.days < days_at_eighteen:
    #         raise ValueError("Регистрация доступна только лицам 18+")
    #     return v



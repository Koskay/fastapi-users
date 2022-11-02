import datetime

from .models import Person


async def validate_birthday(user: Person) -> bool:
    """Проверка пользователя на совершеннолетие"""

    user_birth = user.birth
    user_old = datetime.date.today() - user_birth
    days_at_eighteen = 6574
    return user_old.days > days_at_eighteen



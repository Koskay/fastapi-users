from pydantic import BaseSettings, Field

"""If Not docker. Раскомментировать. Заполнить <...>"""
# SQL_ALCHEMY_URL = f'postgresql://<ваш db_user>:<ваш db_pass>@<ваш db_host>:5432/<ваш db_name>'

class Settings(BaseSettings):
    """If Not docker. Закомментировать"""
    db_url: str = Field(..., env='DATABASE_URL')
        
    """If Not docker. Раскомментировать"""
    # db_url: str = SQL_ALCHEMY_URL)

settings = Settings()


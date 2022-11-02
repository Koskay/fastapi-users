from pydantic import BaseSettings, Field

"""No docker. Раскоментировать"""
# SQL_ALCHEMY_URL = f'postgresql://<ваш db_user>:<ваш db_pass>@<ваш db_host>:5432/<ваш db_name>'

class Settings(BaseSettings):
    """No docker. Закоментировать"""
    db_url: str = Field(..., env='DATABASE_URL')
        
    """No docker. Раскоментировать"""
    # db_url: str = SQL_ALCHEMY_URL)

settings = Settings()


# import os
# from dotenv import load_dotenv
#
# load_dotenv()
#
# DB_NAME = os.getenv('DB_NAME')
# DB_HOST = os.getenv('DB_HOST')
# DB_USER = os.getenv('DB_USER')
# DB_PASSWORD = os.getenv('DB_PASSWORD')
#
# SQL_ALCHEMY_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@db01:5432/postgres'

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_url: str = Field(..., env='DATABASE_URL')


settings = Settings()


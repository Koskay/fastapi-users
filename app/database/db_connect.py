import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

from .config import settings

metadata = sqlalchemy.MetaData()

conn = databases.Database(settings.db_url)

engine = sqlalchemy.create_engine(settings.db_url)


Base = declarative_base()
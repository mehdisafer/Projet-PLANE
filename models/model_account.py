from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from configs.config import *
from sqlalchemy_utils import create_database, database_exists, drop_database

Base = declarative_base()

# Créez un modèle de données
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))


if __name__ == "__main__":
    test = User()
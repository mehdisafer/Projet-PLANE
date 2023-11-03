import os
import pandas as pd
from os.path import join

from sqlalchemy import create_engine

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


DATABASE_HOST = "localhost"
DATABASE_NAME = "account"
DATABASE_USERNAME = "root"
DATABASE_PASSWORD = "root"

engine = create_engine(f"mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}")
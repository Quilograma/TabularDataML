from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Get the environment variables
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
MYSQL_PORT = os.environ.get('MYSQL_PORT')

# Connect to the MySQL database using SQLAlchemy
engine = create_engine(f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@db:{MYSQL_PORT}/{MYSQL_DATABASE}')

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)
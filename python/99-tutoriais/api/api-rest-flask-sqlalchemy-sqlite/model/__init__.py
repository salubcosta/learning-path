from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from model.base import Base

from model.produto import Produto
from model.comentario import Comentario

import os

db_path = "database/"

if not os.path.exists(db_path):
    os.makedirs(db_path)

db_url = f"sqlite:///{db_path}/db.sqlite3"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)

if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)
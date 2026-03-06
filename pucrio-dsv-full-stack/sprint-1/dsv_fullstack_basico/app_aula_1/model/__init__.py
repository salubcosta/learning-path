from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Importar elementos definidos no modelo
from model.base import Base
from model.comentario import Comentario
from model.produto import Produto

# url de acesso ao bd
db_url = 'sqlite:///database/db.sqlite3'

# cria engine
engine = create_engine(db_url, echo=False)

# instancia seção com o db
Session = sessionmaker(bind=engine)

if not database_exists(engine.url):
    create_database(engine.url)

# cria as tabelas
Base.metadata.create_all(engine)
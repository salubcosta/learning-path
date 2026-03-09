from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from model.base import Base

class Produto(Base):
    __tablename__ = 'produto'

    id = Column("pk_produto", Integer, primary_key=True)
    nome = Column(String(80), unique=True)
    quantidade = Column(Integer)
    valor = Column(Float)
    data_insercao = Column(DateTime, default=datetime.now())

    # Infomando para o ORM que há relacionamento entre Comentário e Produto
    comentarios = relationship("Comentario")

    def __init__(self, nome: str, quantidade: int, valor: float):
        """
         Cria um Produto

        Arguments:
            nome: nome do produto.
            quantidade: quantidade que se espera comprar daquele produto
            valor: valor esperado para o produto
            data_insercao: data de quando o produto foi inserido à base
        """
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
        self.data_insercao = datetime.now()

    def adiciona_comentario(self, comentario):
        """ Adiciona um novo comentário ao Produto
        """
        self.comentarios.append(comentario)
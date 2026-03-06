from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base, Comentario

class Produto(Base):
    __tablename__ = 'produto'

    id = Column("pk_produto", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    quantidade = Column(Integer)
    valor = Column(Float)
    data_insercao = Column(DateTime, default=datetime.now())

    # informando relacionamento
    comentarios = relationship("Comentario")

    def __init__(self, nome:str, quantidade: int, valor:float, data_insercao:Union[DateTime, None] = None):
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

        if data_insercao:
            self.data_insercao = data_insercao 
    
    def adiciona_comentario(self, comentario:Comentario):
        """
        Adiciona um comentário ao produto
        """
        self.comentarios.append(comentario)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "quantidade": self.quantidade,
            "valor": self.valor,
            "data_insercao": self.data_insercao
        }
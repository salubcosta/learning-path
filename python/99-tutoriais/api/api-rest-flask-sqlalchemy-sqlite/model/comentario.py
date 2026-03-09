from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from model.base import Base

class Comentario(Base):
    __tablename__ = 'comentario'

    id = Column(Integer, primary_key=True)
    texto = Column(String(200))
    data_insercao = Column(DateTime, default=datetime.now())
    produto = Column(Integer, ForeignKey("produto.pk_produto"), nullable=False)

    def __init__(self, texto):
        """
        Tabela de comentários de produtos

        Arguments:
            texto: Comentário sobre algum produto
        """
        self.texto = texto
        self.data_insercao = datetime.now()
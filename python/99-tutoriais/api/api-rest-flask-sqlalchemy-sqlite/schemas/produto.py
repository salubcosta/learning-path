from pydantic import BaseModel
from typing import Optional, List
from model.produto import Produto
from schemas.comentario import ComentarioSchema

class ProdutoSchema(BaseModel):
    """ Define um exemplo de produto a ser inserido
    """
    nome: str = "Mouse"
    quantidade: Optional[int] = 10
    valor: float = 39.90

class ProdutoBuscaSchema(BaseModel):
    """ Define um exemplo de busca por nome
    """
    nome : str = "Mouse"

class ListagemProdutoSchema(BaseModel):
    """ Define uma listagem de produto
    """
    produtos : List[ProdutoSchema]

class ProdutoViewSchema(BaseModel):
    """ Define como um produto será retornado
    """
    id: int = 1
    nome: str = "Mouse"
    quantidade: int = 10
    valor: float = 39.90
    total_comentarios: int = 1
    comentarios: List[ComentarioSchema]

class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura de dado retornado após uma requisição
    """
    message: str
    nome: str

def apresenta_produtos(produtos):
    result = []

    for produto in produtos:
        result.append({
            "id": produto.id,
            "nome": produto.nome,
            "quantidade": produto.quantidade,
            "valor": produto.valor
        })
    
    return {"produtos": result}

def apresenta_produto(produto):
    """ Define uma representacao do produto seguindo o schema definido em ProdutoViewSchema
    """
    return {
        "id": produto.id,
        "nome": produto.nome,
        "quantidade": produto.quantidade,
        "valor": produto.valor,
        "total_comentarios": len(produto.comentarios),
        "comentarios": [{"texto": c.texto} for c in produto.comentarios]
    }
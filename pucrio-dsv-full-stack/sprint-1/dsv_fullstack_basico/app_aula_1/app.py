from flask import Flask, request, jsonify
from sqlalchemy.exc import IntegrityError

from model import Session, Produto
from model.comentario import Comentario

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Home page"}), 200

@app.route('/add_produto', methods=['POST'])
def add_produto():
    session = Session()
    data = request.get_json()
    
    success_msg = "Produto adicionado com sucesso!"
    error_msg = ["Não foi possível salvar novo item :/", "Produto de mesmo nome já existe!"]
    
    try:
        if data.get("nome") and data.get("quantidade") and data.get("valor"):
            produto = Produto(
            nome=data.get("nome"),
            quantidade=data.get("quantidade"),
            valor=data.get("valor")
            )
            session.add(produto)
            session.commit()
            return jsonify({"message": success_msg}), 200
        else:
            return jsonify({'message': error_msg[0]}), 400
    except IntegrityError as e:
        return jsonify({"message": error_msg[1]}),400
    except Exception as e:
        print(str(e))
        return jsonify({"message": error_msg[0]}), 400
    finally:
        session.close()
    
@app.route('/get_produto/<produto_id>', methods=['GET'])
def get_produto(produto_id):
    session = Session()
    try:
        produto = session.query(Produto).filter(Produto.id == produto_id).first()

        if not produto:
            return jsonify({"message": "Produto não encontrado!"}), 404
        else:
            return jsonify({"produto": produto.to_dict()})
    finally:
        session.close()
    
@app.route('/get_produtos', methods=['GET'])
def get_produtos():
    session = Session()
    try:
        lista_de_produto = [p.to_dict() for p in session.query(Produto).all()]

        if lista_de_produto:
            output = {
                "produtos": lista_de_produto,
                "total": len(lista_de_produto)
            }
            return jsonify(output)
        else:
            return jsonify({"message": "Nenhum produto encontrado!"}), 404
    finally:
        session.close()
    
@app.route('/remover_produto/<produto_id>', methods=['DELETE'])
def remover_produto(produto_id):
    session = Session()
    try:
        count = session.query(Produto).filter(Produto.id == produto_id).delete()
        session.commit()

        if count == 1:
            return jsonify({"message": "Produto removido!"})
        else:
            return jsonify({"message": "Produto não encontrado!"}), 404
    finally:
        session.close()
    
@app.route('/add_comentario/<produto_id>', methods=['POST'])
def add_comentario(produto_id):
    session = Session()
    try:
        produto = session.query(Produto).filter(Produto.id == produto_id).first()

        if not produto:
            return jsonify({"message": "Produto não encontrado!"}), 404
        else:
            data = request.get_json()
            autor = data.get('autor')
            texto = data.get('texto')
            n_estrelas = data.get('n_estrela')
            if n_estrelas:
                n_estrelas = int(n_estrelas)
            
            comentario = Comentario(autor=autor, texto=texto, n_estrela=n_estrelas)
            produto.adiciona_comentario(comentario=comentario)
            session.commit()

            return jsonify({"message": "Comentário adicionado!"})
    finally:
        session.close()
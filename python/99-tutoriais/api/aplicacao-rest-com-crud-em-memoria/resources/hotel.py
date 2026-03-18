from flask_restful import Resource, reqparse
from models import HotelModel

hoteis_db = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Brasília'
    },
    {
        'hotel_id': 'bravo',
        'nome': 'Bravo Hotel',
        'estrelas': 4.4,
        'diaria': 800.34,
        'cidade': 'Palmas'
    },
    {
        'hotel_id': 'charlie',
        'nome': 'Charlie Hotel',
        'estrelas': 3.9,
        'diaria': 320.34,
        'cidade': 'Araguaína'
    }
]
class Hoteis(Resource):
    def get(self,):
        return {'hoteis': hoteis_db}
    
class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
    
    def find_hotel(self, hotel_id):
        for hotel in hoteis_db:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        resultado = self.find_hotel(hotel_id=hotel_id)

        if not resultado:
            return {'message': 'Hotel not found.'}, 404
        return resultado, 200
    
    def post(self, hotel_id):
        dados = self.argumentos.parse_args()

        novo_hotel = HotelModel(hotel_id=hotel_id, **dados)
        # novo_hotel = {'hotel_id': hotel_id, **dados}

        hoteis_db.append(novo_hotel.json())

        return novo_hotel.json(), 200
    
    def put(self, hotel_id):
        dados = self.argumentos.parse_args()
        # novo_hotel = {'hotel_id': hotel_id, **dados }
        novo_hotel = HotelModel(hotel_id=hotel_id, **dados)
        hotel = self.find_hotel(hotel_id=hotel_id)
        
        if hotel:
            hotel.update(novo_hotel.json())
            return hotel, 200
        
        hoteis_db.append(novo_hotel.json())
        return novo_hotel.json(), 201

    def delete(self, hotel_id):
        hotel = [hotel for hotel in hoteis_db if hotel['hotel_id'] == hotel_id]

        if not hotel:
            return {'message': 'Hotel não encontrado.'}, 404

        hoteis_db.remove(*hotel)

        return {'message': 'Hotel removido com sucesso.'}
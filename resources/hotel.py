from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hotels = [
    {
    'hotel_id': 'alpha',
    'name': 'Alpha Hotel',
    'star': 4.3,
    'price': 420.34,
    'city': 'Rio de Janeiro',
    },
    {
    'hotel_id': 'bravo',
    'name': 'Bravo Hotel',
    'star': 4.4,
    'price': 380.90,
    'city': 'Santa Catarina',
    },
    {
    'hotel_id': 'charlie',
    'name': 'Charlie Hotel',
    'star': 3.9,
    'price': 320.2,
    'city': 'Santa Catarina',
    },
]

class Hotels(Resource):
    def get(self):
        return hotels
    

class Hotel(Resource):
    args = reqparse.RequestParser()
    args.add_argument('name')
    args.add_argument('star')
    args.add_argument('price')
    args.add_argument('city')
    
    @classmethod
    def find_hotel(cls, hotel_id):
        hotel = [hotel for hotel in hotels if hotel.get('hotel_id') == hotel_id]
        hotel = hotel[0] if hotel else None

        return hotel
    
    def get(self, hotel_id: str):
        hotel = Hotel.find_hotel(hotel_id)
        print(hotel)
        
        if hotel:
            code = 200
            return hotel, code
        else:
            code = 404
            return {'message': 'Hotel not found.'}, code
    
    def post(self, hotel_id):
        data = self.args.parse_args()

        math_hotel = Hotel.find_hotel(hotel_id)

        if not math_hotel:
            hotel = HotelModel(
                hotel_id = hotel_id,
                **data
            )

            hotels.append(hotel.json())

            return hotel.json(), 200
        
        return {'message': 'duplicate data.'}, 400
    
    def put(self, hotel_id):
        data = self.args.parse_args()

        match_hotel = Hotel.find_hotel(hotel_id)

        if match_hotel:
            hotel = HotelModel(
                hotel_id,
                **data
            )

            match_hotel.update(
                {
                    **hotel.json()
                }
            )

            code = 200
            return match_hotel, code
        else:
            hotel = {
                "hotel_id": hotel_id,
                **data
            }

            hotels.append(hotel)

            code = 201
            return hotel, code

    def delete(self, hotel_id):
        global hotels
        hotels = [hotel for hotel in hotels if hotel['hotel_id'] != hotel_id]

        code = 200
        return {'message': 'hotel deleted'}, code


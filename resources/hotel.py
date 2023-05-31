from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from sql_alchemy import database

class Hotels(Resource):
    def get(self):
        return HotelModel.all_hotels()
    

class Hotel(Resource):
    args = reqparse.RequestParser()
    args.add_argument('name')
    args.add_argument('star')
    args.add_argument('price')
    args.add_argument('city')
    
    def get(self, hotel_id: str):
        hotel = HotelModel.find_hotel(hotel_id)
        
        if hotel:
            code = 200
            return hotel.json(), code
        else:
            code = 404
            return {'message': 'Hotel not found.'}, code
    
    def post(self, hotel_id):
        data = self.args.parse_args()

        math_hotel = HotelModel.find_hotel(hotel_id)

        if not math_hotel:
            hotel = HotelModel.create_hotel(
                hotel_id = hotel_id,
                **data
            )

            return hotel.json(), 201
        
        return {'message': 'Hotel already exists.'}, 400
    
    def put(self, hotel_id):
        data = self.args.parse_args()

        hotel = HotelModel.find_hotel(hotel_id)

        if hotel:
            hotel.update_hotel(
                **data
            )

            code = 200
        else:
            hotel = HotelModel.create_hotel(
                hotel_id = hotel_id,
                **data
            )

            code = 201        
                    
        return hotel.json(), code

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)

        if hotel:
            hotel.delete_hotel()

            msg = {'message': 'Hotel deleted.'}
            code = 200
        else:
            msg = {'message': 'Hotel not found.'}
            code = 404
        
        return msg, code


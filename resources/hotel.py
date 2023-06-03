from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required

class Hotels(Resource):
    def get(self):
        return HotelModel.all_hotels()
    

class Hotel(Resource):
    args = reqparse.RequestParser()
    args.add_argument('name', type = str, required = True, help = "The field 'name' cannot be left blank.")
    args.add_argument('star', type = float)
    args.add_argument('price', type = float)
    args.add_argument('city', type = str, required = True, help = "The field 'city' cannot be left blank.")
    
    def get(self, hotel_id: str):
        hotel = HotelModel.find_hotel(hotel_id)
        
        if hotel:
            code = 200
            return hotel.json(), code
        else:
            code = 404
            return {'message': 'Hotel not found.'}, code
    
    @jwt_required()
    def post(self, hotel_id):
        data = self.args.parse_args()

        math_hotel = HotelModel.find_hotel(hotel_id)

        if not math_hotel:
            try:
                hotel = HotelModel.create_hotel(
                    hotel_id = hotel_id,
                    **data
                )

            except:
                return {'message': 'An internal error ocurred trying to save hotel.'}, 500

            return hotel.json(), 201
        
        return {'message': 'Hotel already exists.'}, 400
    
    @jwt_required()
    def put(self, hotel_id):
        data = self.args.parse_args()

        hotel = HotelModel.find_hotel(hotel_id)

        if hotel:
            try:
                hotel.update_hotel(
                    **data
                )

                code = 200
            except:
                return {'message': 'An internal error ocurred trying to update hotel.'}, 500
            
        else:
            try:
                hotel = HotelModel.create_hotel(
                    hotel_id = hotel_id,
                    **data
                )

                code = 201
            except:
                return {'message': 'An internal error ocurred trying to save hotel.'}, 500        
                    
        return hotel.json(), code

    @jwt_required()
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)

        if hotel:
            try:
                hotel.delete_hotel()

                msg = {'message': 'Hotel deleted.'}
                code = 200
            except:
                return {'message': 'An internal error ocurred trying to delete hotel.'}, 500

        else:
            msg = {'message': 'Hotel not found.'}
            code = 404
        
        return msg, code


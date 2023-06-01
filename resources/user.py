from flask_restful import Resource, reqparse
from models.user import UserModel

class User(Resource):
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        
        if user:
            code = 200
            return user.json(), code
        
        code = 404
        return {'message': 'User not found.'}, code
    
    def delete(self, user_id):
        user = UserModel.find_user(user_id)

        if user:
            user.delete_user()
            
            code = 200
            return {'message': 'User deleted.'}, code

        code = 404
        return {'message': "User not found."}, code
    
class UserRegister(Resource):
    def post(self):
        args = reqparse.RequestParser()
        args.add_argument('username', type = str, required = True, help = "The field 'username' cannot be left blank")
        args.add_argument('password', type = str, help = "The field 'password' cannot be left blank")
        data = args.parse_args()

        user = UserModel.create_user(**data)

        code = 201
        return user.json(), code


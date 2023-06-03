from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import create_access_token, jwt_required

class User(Resource):
    
    @jwt_required()
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        
        if user:
            code = 200
            return user.json(), code
        
        code = 404
        return {'message': 'User not found.'}, code
    
    @jwt_required()
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
        
        user = UserModel.query.filter_by(username = data.username).first()

        if not user:
            user = UserModel.create_user(**data)

            code = 201
            return user.json(), code

        code = 400
        return {"message": "The user '{}' already exists.".format(data.username)}, 400

class UserLogin(Resource):
    @classmethod
    def post(cls):
        args = reqparse.RequestParser()
        args.add_argument('username', type = str, required = True, help = "This field cannot be left blank.")
        args.add_argument('password', type = str, required = True, help = "This field cannot be left blank.")

        data = args.parse_args()
        user = UserModel.query.filter_by(username=data.username).first()
        
        if user and user.hash == data.password:
            access_token = create_access_token(user.user_id)
            code = 200
            return {
                "message": "Login is successful.",
                "access_token": access_token
            }, code
        
        return {"message": "invalid user or password."}



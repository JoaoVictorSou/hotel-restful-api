from flask import Flask
from flask_restful import Resource, Api
from sql_alchemy import database
from config import settings
import os

APPLICATION_PORT = os.environ.get('PORT')
CONNECT_STRING = os.path.join(
    os.path.abspath("."),
    settings.DATABASE_PATH
)

# Instância do Flask
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{CONNECT_STRING}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Integração com extensões do Flask
api = Api(app)
"""
Na utilização abaixo, o SQLAlchemy já está instanciado em outro módulo.
De forma que o método init_app possibilita que ele seja integrado ao Flask,
sem que essa instância seja necessariamente alocada neste arquivo - o principal.
"""
database.init_app(app)

from resources.hotel import Hotels, Hotel
api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotels/<string:hotel_id>')

from resources.user import User, UserRegister, UserLogin
api.add_resource(User, '/users/<int:user_id>')
api.add_resource(UserRegister, '/users')
api.add_resource(UserLogin, '/login')

with app.app_context():
    database.create_all()

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=APPLICATION_PORT, debug=True
    )
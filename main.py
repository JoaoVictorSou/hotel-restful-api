from flask import Flask
from flask_restful import Resource, Api
import os

APPLICATION_PORT = os.environ.get('PORT')

app = Flask(__name__)
api = Api(app)

from resources.hotel import Hotels, Hotel
api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotels/<string:hotel_id>')

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=APPLICATION_PORT, debug=True
    )
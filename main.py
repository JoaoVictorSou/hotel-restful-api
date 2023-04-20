from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

from resources.hotel import Hotels, Hotel
api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotels/<string:hotel_id>')

if __name__ == '__main__':
    app.run(port=3000, debug=True)
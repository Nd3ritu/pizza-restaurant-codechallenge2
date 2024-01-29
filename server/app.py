from flask import Flask, jsonify, request,make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS

from models import db, Restaurant ,Pizza, RestaurantPizza

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///respizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

CORS(app)
migrate = Migrate(app,db)
db.init_app(app)
api = Api(app)

class Index(Resource):
    def get(self):
        response_body = {
            "index":"Pizza-Restaurant API"
        }

        return make_response(jsonify(response_body),200)
api.add_resource(Index, '/')



if __name__ == '__main__':
    app.run(port=5555)
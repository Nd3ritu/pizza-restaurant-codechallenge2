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

class RestaurantResource(Resource):
    def get(self):
        restaurants = [
            {
                'id': restaurant.id,
                'name': restaurant.name,
                'address': restaurant.address
            }
            for restaurant in Restaurant.query.all()]

        return make_response(jsonify(restaurants), 200)

api.add_resource(RestaurantResource,'/restaurants')

class OneRestaurant(Resource):
    def get(self,id):

        restaurant = Restaurant.query.filter_by(id=id).first()

        if restaurant:
            data ={
                "id":restaurant.id,
                "name":restaurant.name,
                "address":restaurant.address,
                "pizzas":[
                    {
                        "id": restaurantpizza.pizza_id,
                        "price":restaurantpizza.price,
                        
                    }
                    for restaurantpizza in restaurant.restaurantpizzas
                ]
            }

            return data
        return {
            "error": "Restaurant not found"
        }
    def delete(self,id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
            RestaurantPizza.query.filter_by(restaurant_id=id).delete()
            db.session.delete(restaurant)
            db.session.commit()
            return '', 204
        else:
            return make_response(jsonify({"error":"Restaurant not found therefore can't delete"}))
api.add_resource(OneRestaurant,'/restaurants/<int:id>')

if __name__ == '__main__':
    app.run(port=5555)

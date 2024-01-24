from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import CheckConstraint

db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    serialize_rules = ('-restaurantpizzas.restaurant')
    
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurantpizzas = db.relationship('RestaurantPizza', backref ='restaurant')

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    serialize_rules = ('-restaurantpizzas.pizza',)

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    restaurantpizzas = db.relationship('RestaurantPizza', backref='pizza')

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurantpizzas'

    serialize_rules = ('-restaurant.restaurantpizzas', '-pizza.resturantpizza')

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"))
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizzas.id"))
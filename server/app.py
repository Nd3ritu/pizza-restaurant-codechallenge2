from flask import Flask, jsonify, request,make_response
from flask_migrate import Migrate

from flask_cors import CORS
from sqlalchemy.exc import IntegrityError

from models import db, Restaurant

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///respizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

CORS(app)
migrate = Migrate(app,db)
db.init_app(app)

@app.route('/')
def index():
    response_body = {"Message":"This restaurant-pizza API"}
    return make_response(jsonify(response_body), 200)
from flask import Flask, jsonify
from flask_restful import Api
import os
# from flask_jwt_extended import JWTManager
from flask_jwt import JWT
from flask_migrate import Migrate
from resources.user import UserRegister, User, UserLogin
from security import authenticate, identity
from config import Config
from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin

# from sqlalchemy.sql import text
from db import db

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = "jose"
api = Api(app)
# jwt = JWTManager(app)
jwt = JWT(app, authenticate, identity)
db.init_app(app)
migrate = Migrate(app, db)

# @app.before_first_request
# def create_tables():
#     db.create_all()

spec = APISpec(
    title='flask-api-swagger-doc',
    version='1.0.0',
    openapi_version='3.0.2',
    plugins=[FlaskPlugin(), MarshmallowPlugin()]
)


@app.route('/api/swagger.json')
def create_swagger_spec():
    return jsonify(spec.to_dict())


@app.route('/')
def hello():
    return "This is 'user' flask REST API"


api.add_resource(UserRegister, '/register')
api.add_resource(User, "/user/<int:user_id>")
api.add_resource(UserLogin, "/login")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5555))
    app.run(debug=True, host='0.0.0.0', port=port)

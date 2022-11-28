from flask import Flask, jsonify, render_template, send_from_directory, redirect
from flask_restful import Api
import os
# from flask_jwt_extended import JWTManager
from flask_jwt import JWT
from flask_migrate import Migrate
from flasgger import Swagger, swag_from

from resources.user import UserRegister, User, UserAuthCheck, UserList
from security import authenticate, identity
from config import Config
from db import db

app = Flask(__name__, template_folder='swagger/templates')
app.config.from_object(Config)
app.secret_key = "jose"
jwt = JWT(app, authenticate, identity)
db.init_app(app)
api = Api(app, prefix="/api")
migrate = Migrate(app, db)

# @app.before_first_request
# def create_tables():
#     db.create_all()

template = {
    "swagger": "2.0",
    "info": {
        "title": "User API",
        "description": "API for User application",
        "version": "0.1.0"
    },
    "host": f"{os.environ.get('USER_APP_URL')}:{os.environ.get('USER_APP_PORT')}",
    # "basePath": "/api",
    "schemes": ["http", "https"],
    "securityDefinitions": {
        "Bearer":
            {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "Description: jwt *your_jwt_token...*"
            }
    },
}

swagger = Swagger(app, template=template)


@app.route('/')
def hello():
    text = '<a href="/apidocs/#/">/apidocs/#/</a>'
    return f"This is 'user' flask REST API. <br>Swagger is here {text}"


@app.route('/auth', methods=["POST"])
@swag_from('docs/login.yaml')
def auth():
    pass


api.add_resource(UserRegister, '/register')
api.add_resource(User, "/users/<int:user_id>")
api.add_resource(UserList, "/users")
api.add_resource(UserAuthCheck, "/user-auth-check")
# api.add_resource(UserLogin, "/login")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5555))
    # app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=port)

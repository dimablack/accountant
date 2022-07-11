"""
User resource
"""
from flask import request
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from libs.strings import gettext, gettext_message
from models.user import UserModel
from schemas.users import UserSchema

user_schema = UserSchema()


class UserRegister(Resource):
    """User Register resource"""

    @classmethod
    def post(cls):
        user_json = request.get_json()
        user = user_schema.load(user_json)

        if UserModel.find_by_username(user.username):
            if UserModel.find_by_email(user.email):
                return gettext_message("user_email_exists"), 400
            return gettext_message("user_username_exists"), 400

        user.save_to_db()

        return gettext_message("user_registered"), 400


class User(Resource):
    """User resource for authenticated requests"""
    @classmethod
    @jwt_required()
    def get(cls, user_id: int):
        """Find and return User model by id"""
        user = UserModel.find_by_id(user_id)
        if not user:
            return gettext_message("user_not_found"), 404

        return user_schema.dump(user), 200

    @classmethod
    @jwt_required
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return gettext_message("user_not_found"), 404

        user.delete_from_db()
        return gettext_message("user_deleted"), 200

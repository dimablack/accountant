"""
User resource
"""
from flask import request, Response
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from flasgger import swag_from

# import app
from libs.strings import gettext, gettext_message
from models.user import UserModel
from schemas.users import UserSchema

user_schema = UserSchema()
user_list_schema = UserSchema(many=True)


class UserRegister(Resource):
    """User Register resource"""

    @classmethod
    @swag_from('../docs/register.yaml')
    def post(cls):
        user_json = request.get_json()
        user = user_schema.load(user_json)

        if UserModel.find_by_username(user.username):
            if UserModel.find_by_email(user.email):
                return gettext_message("user_email_exists"), 400
            return gettext_message("user_username_exists"), 400

        user.save_to_db()

        return gettext_message("user_registered"), 200


class User(Resource):
    """User resource for authenticated requests"""

    @classmethod
    @jwt_required()
    @swag_from('../docs/get_user.yaml')
    def get(cls, user_id: int):
        """Find and return User model by id"""
        user = UserModel.find_by_id(user_id)
        if not user:
            return gettext_message("user_not_found"), 404

        return user_schema.dump(user), 200

    @classmethod
    @jwt_required()
    def delete(cls, user_id: int):
        """Delete user from db"""
        user = UserModel.find_by_id(user_id)
        if not user:
            return gettext_message("user_not_found"), 404

        user.delete_from_db()
        return gettext_message("user_deleted"), 200


class UserList(Resource):
    """User List resource for authenticated requests"""

    @classmethod
    @jwt_required()
    @swag_from('../docs/get_all_users.yaml')
    def get(cls):
        """Return list of all users from db"""
        return {"data": user_list_schema.dump(UserModel.find_all())}, 200


class UserAuthCheck(Resource):

    @jwt_required()
    @swag_from('../docs/user_auth_check.yaml')
    def get(self):
        """Check if user is authenticated"""
        return Response(status=200)

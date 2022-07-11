from hmac import compare_digest
from models.user import UserModel


def authenticate(username_or_email, password):
    """Authenticate user in the system via username or email."""
    user_by_username = UserModel.find_by_username(username_or_email)
    if user_by_username and compare_digest(user_by_username.password, password):
        return user_by_username
    else:
        user_by_email = UserModel.find_by_email(username_or_email)
        if user_by_email and compare_digest(user_by_email.password, password):
            return user_by_email


def identity(payload):
    """Find and return User by ID"""
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

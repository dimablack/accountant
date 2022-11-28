"""
User database model.
"""
from db import db, CustomSchema


class UserModel(db.Model):
    """User in the system."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password = db.Column(db.String(128))

    __table_args__ = {
        "schema": CustomSchema.CUSTOM_SCHEMA
    }

    def __repr__(self):
        return f'<User {self.username}>'

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        """Find and return User by username"""
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        """Find and return User by email"""
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id):
        """Find and return User by ID"""
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["UserModel"]:
        """Find and return all Users from db"""
        return cls.query.all()

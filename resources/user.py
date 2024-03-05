from http.client import FORBIDDEN
import secrets
from flask import jsonify, request
from models import ApiKey


def require_admin(func):
    def wrapper(*args, **kwargs):
        key_hash = ApiKey.key_hash(request.headers.get("CustomWorkout-Api-Key").strip())
        db_key = ApiKey.query.filter_by(admin=True).first()
        if secrets.compare_digest(key_hash, db_key.key):
            return func(*args, **kwargs)
        raise FORBIDDEN
    return wrapper

def require_user_key(func):
    def wrapper(self, user, *args, **kwargs):
        key_hash = ApiKey.key_hash(request.headers.get("CustomWorkout-Api-Key").strip())
        db_key = ApiKey.query.filter_by(user=user).first()
        if db_key is not None and secrets.compare_digest(key_hash, db_key.key):
            return func(*args, **kwargs)
        raise FORBIDDEN
    return wrapper
from http.client import FORBIDDEN
import random
import secrets
import string
from flask import jsonify, request
from models import ApiKey, User
from extensions import db


def generate_api_key():
    """Generate a random API key."""
    key_length = 32 
    characters = string.ascii_letters + string.digits
    api_key = ''.join(random.choice(characters) for _ in range(key_length))
    return api_key

def assign_api_key_to_user(user_id):
    """Assign a generated API key to the specified user."""
    user = User.query.get(user_id)
    if user:
        api_key = generate_api_key()
        hashed_key = ApiKey.key_hash(api_key)
        new_api_key = ApiKey(key=hashed_key, user_id=user_id)
        db.session.add(new_api_key)
        db.session.commit()
        return api_key
    else:
        return None
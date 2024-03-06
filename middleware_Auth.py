from http.client import FORBIDDEN
import secrets
from flask import jsonify, request, g
from extensions import db
from data_models.models import ApiKey 

def authenticate():
    if request.endpoint != 'static':
        api_key = request.headers.get('X-API-Key')
        print("Received API key:", api_key)
        if not api_key:
            return jsonify({'error': 'API key is missing'}), 401
        api_key_object = ApiKey.query.filter_by(key=api_key).first() # remove later
        if not api_key_object:
            return jsonify({'error': 'Invalid API key'}), 401
        g.current_api_key = api_key_object
        print("Current API key object:", g.current_api_key) # remove later

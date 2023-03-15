from mongoengine import ( Document, StringField, EmailField,)
from flask_bcrypt import generate_password_hash, check_password_hash
import datetime

class Users(Document):
    """
    Template for a mongoengine document, which represents a user.
    Password is automatically hashed before saving.
    :param email: unique required email-string value
    :param password: required string value, longer than 6 characters
    :param name: option unique string username
    """
    email = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=6, regex=None)
    name = StringField(unique=False)

    def generate_pw_hash(self):
        self.password = generate_password_hash(password=self.password).decode('utf-8')
    
    #BCrypt for password hashing
    generate_pw_hash.__doc__ = generate_password_hash.__doc__

    def check_pw_hash(self, password: str) -> bool:
        return check_password_hash(pw_hash=self.password, password=password)
    
    #BCrypt for password hashing
    check_pw_hash.__doc__ = check_password_hash.__doc__

    def save(self, *args, **kwargs):
        # Overwrite Document save method to generate password hash prior to saving
        if self._created:
            self.generate_pw_hash()
        super(Users, self).save(*args, **kwargs)
    
    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

from mongoengine import ( Document, StringField, DateTimeField,)


class Chat_History(Document):
    """
    Template for a mongoengine document, which represents a user.
    Password is automatically hashed before saving.
    :param user_id: unique required login value
    :param chat_id: unique required chat id
    :param query: question to ask chatbot
    :param response: chatbot response
    :param documentId: required unique document id
    :param timestamp: timestamp of entry
    """
    
    user_id = StringField(required=True, unique=True)
    chat_id = StringField(required=True, unique=True)
    query = StringField(required=True)
    response = StringField(required=True)
    document_id = StringField(required=True, unique=True)
    timestamp = DateTimeField()
    
    
    
    
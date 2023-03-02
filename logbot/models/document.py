from mongoengine import ( Document, StringField, DateTimeField,)


class User_Document(Document):
    """
    Template for a mongoengine document, which represents a user.
    Password is automatically hashed before saving.
    :param user_id: unique required login value
    :param documentId: required unique document id
    :param document_content: option unique string username
    :param document_summary: string representation of documents summary
    :param timestamp: timestamp of entry
    """
    
    user_id = StringField(required=True, unique=True)
    document_id = StringField(required=True, unique=True)
    document_content = StringField(max_length=6000)
    document_summary = StringField(max_length=6000)
    timestamp = DateTimeField()
    
    
    
    
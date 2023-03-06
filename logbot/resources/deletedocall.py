from flask import  request,  Response, abort
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
# project resources
from models.users import Users
from models.document import User_Document
from models.chat_history import Chat_History
import json
import uuid
from resources.errors import user_not_found, resource_already_exists

class DelDoc(Resource):
    @staticmethod
    @jwt_required()
    def delete() -> Response:
        
        authorized: bool = Users.objects.get(id=get_jwt_identity())
        
        if authorized:
            user_details= json.loads(Users.objects.get(id=get_jwt_identity()).to_json())

            print(user_details['user_id'])
            if not request.json:
                abort(415)
                
            data = request.get_json()
            doc_count = User_Document.objects(document_id=data.get('document_id')).count()
            
            if doc_count != 0:
                if data["deletedoc"] == "True":
                    User_Document.objects(document_id=data.get('document_id')).delete()
                    Chat_History.objects(document_id=data.get('document_id')).delete()
                    data_load_chat = {"user_id": [], "chat_id":[],"query":[],"response":[], 'document_id' : []}
                    data_load_chat['user_id'] = user_details['user_id']
                    data_load_chat['chat_id']=  str(uuid.uuid4()) +"CHAT"
                    data_load_chat['query'] = "delete document and chat history"
                    data_load_chat['response'] = "Document with document id " + data.get('document_id') + ' and corresponding chat history deleted'
                    data_load_chat['document_id'] = str(uuid.uuid4())
                    chat_load = Chat_History(**data_load_chat)
                    chat_load.save()
                    session_response = {'message' : data_load_chat['response']} 
            else: 
                    session_response = {'message' : 'Document and chat history already deleted'}
        return Response(json.dumps(session_response), 200)
    
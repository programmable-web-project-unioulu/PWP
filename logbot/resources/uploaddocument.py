from flask import  request,  jsonify, Response
from werkzeug.utils import secure_filename
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
# project resources
from models.users import Users
from models.document import User_Document
from models.chat_history import Chat_History
import json
import uuid
import textract
from resources.errors import user_not_found, resource_already_exists
ALLOWED_EXTENSIONS = set(['txt'])


def allowed_file(filename):
 return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class UploadFile(Resource):
    @staticmethod
    @jwt_required()
    def post() -> Response:

        authorized: bool = Users.objects.get(id=get_jwt_identity())
        if authorized:
            user_details= json.loads(Users.objects.get(id=get_jwt_identity()).to_json())

            print(user_details['user_id'])
            if 'file' not in request.files:
                resp = jsonify({'message' : 'No file part in the request'})
                resp.status_code = 400
                return resp
            file = request.files['file']
            if file.filename == '':
                resp = jsonify({'message' : 'No file selected for uploading'})
                resp.status_code = 400
                return resp
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(filename)
                data_load = {"user_id": [],"document_id":[],"document_name":[],"document":[], 'document_summary' : [],'document_tag' : []}
                data_load['user_id'] = user_details['user_id']
                data_load['document_id'] =  str(uuid.uuid4()) +"DOC"
                data_load['chat_id']= str(uuid.uuid4()) +"CHAT"
                data_load['document_name'] = str(filename)
                data_load['document'] = str(textract.process(filename, encoding='ascii'), 'ascii')
                data_load['document_summary'] = "No summary generation requested"
                data_load['document_tag'] = "No tag generation requested"
                doc_load = User_Document(**data_load)
                doc_load.save()
                data_load_chat = {"user_id": [], "chat_id":[],"query":[],"response":[], 'document_id' : []}
                data_load_chat['user_id'] = user_details['user_id']
                data_load_chat['chat_id']= data_load['chat_id']
                data_load_chat['query'] = "upload log file"
                data_load_chat['response'] = 'File successfully uploaded. Opt for Summary and classification tag generation'
                data_load_chat['document_id'] = data_load['document_id']
                chat_load = Chat_History(**data_load_chat)
                chat_load.save()
                session_response = {'message' : data_load_chat['response'], 'document_id': data_load['document_id'], 'summary' : data_load['document_summary'], 'Classified-Tag' :  data_load['document_tag'] }
                return Response(json.dumps(session_response), 200)
            else: 
                resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'}) 
                resp.status_code = 400 
                return resp

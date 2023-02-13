#!/usr/bin/env python
# coding: utf-8

# In[0]:
#------------------------------------------------------------------------------
# Application for model class
#------------------------------------------------------------------------------
# Date: 13/2/23
# Author: LogBot
#------------------------------------------------------------------------------
# 0.1   LogBot    13-2-23    Initial Draft
#------------------------------------------------------------------------------
# In[1]:
   
import pymongo
import pandas as pd
import uuid
import os
import regex as re
import textract
from datetime import datetime
import DOCPROC as dp


client = pymongo.MongoClient("mongodb://128.214.254.176:27017/")
db = client["logbotdatabase"]

#Define the "login" collection
login_col = db["loginprofile"]

#Define the "chat_history" collection
chat_history_collection = db["chat_history"]

# Define the "documents" collection
documents_collection = db["documents_data"]

#Define the "small_talk" collection
small_talk_collection = db["small_talk"]


def connectdb_read(userid_email):

    query_profile = { "userid_email": userid_email }
    res_doc = pd.DataFrame( list(login_col.find(query_profile)))
    new_user = False
    
    if len(res_doc) == 0:
         loginid =str(uuid.uuid4()) +"LOGIN"
         new_user = True
         
    else:
         loginid = res_doc['loginid'] [0]
    return loginid, new_user


def loginfunc(userid_email, username):
    
    #connect db and get loginId
    loginid, new_user = connectdb_read(userid_email)
    if new_user:
        insert_data = {
                       "loginid": loginid,
                       "username": username,
                       "userid_email": userid_email,
                       "timestamp": datetime.now()
                       }
        
        login_col.insert_one(insert_data)
        
        chatid =str(uuid.uuid4()) +"CHAT"
        query = "greetings"
        reponse_value = "Hello " + username + ". " +"Welcome to LogBot, Please share your log file for analysis"
        documentid = None
        
        insert_chat = {
                       "loginid": loginid,
                       "chatid" : chatid,
                       "query": query,
                       "response": reponse_value,
                       "timestamp": datetime.now(),
                       "documentid": documentid
                       }
        
        chat_history_collection.insert_one(insert_chat)
        
    else:
        query_chat = {
                      "loginid": loginid
                     }
        chat_data_list = pd.DataFrame( list(chat_history_collection.find(query_chat)))
        reponse_value = chat_data_list
        print(chat_data_list)
    return reponse_value 


def homefunc(loginid, datafile, query):
    
    if datafile == 0:
        nofile = True
    else:
       
        content    = str(textract.process(datafile, encoding='ascii'), 'ascii')
        chatid  = str(uuid.uuid4()) +"CHAT"
        query   = "file input"
        response = "summary generated"
        documentid = str(uuid.uuid4()) +"DOC"
        
        insert_chat = {
                       "loginid": loginid,
                       "chatid" : chatid,
                       "query": query,
                       "response": response,
                       "timestamp": datetime.now(),
                       "documentid": documentid
                       }
        chat_history_collection.insert_one(insert_chat)
        
        summaryofdocument = "response summary"
        insert_doc = {
                       "loginid": loginid,
                       "chatid" : chatid,
                       "documentid": documentid,
                       "content": content,
                       "timestamp": datetime.now(),
                       "documentid": documentid,
                       "summaryofdocument": summaryofdocument
                       }
        documents_collection.insert_one(insert_doc)
        
    if nofile:
        
        small_talk_query = { "query" : query}
        response_value_small = pd.DataFrame( list(small_talk_collection.find(small_talk_query)))
        if len(response_value_small) == 0:
            response_value = "Sorry there is no clarity in your question"
    else:
            response_value = dp.document_process(content)
        
    return response_value
   
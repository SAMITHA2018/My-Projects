import logging
import urllib 
from flask_pymongo import pymongo
from flask import jsonify, request
from pymongo import MongoClient

con_string = "mongodb+srv://samitha:<password>@cluster0.s73g17h.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(con_string )
db = client['sample']
user_collection = db['demo'] 


print("Congratulations!! MongoDB connected Successfully")


def project_api_routes(endpoints):
    @endpoints.route('/hello',methods=['GET'])
    def connection():
            str = "Hello SAMITHA!"
            print("Hello SAMITHA!")
            return str
    @endpoints.route('/add_user',methods=["POST"])
    def add_user():
        response={}
        try:
            request_body=request.json
            user_collection.insert_one(request_body)
            print(" successfully added.")
            status= {
                "statusCode":"200",
                "statusMessage": "Success"
            }
        except Exception as e:
            print(e)
            status= {
                "statusCode":"400",
                "statusMessage": str(e)
            }
        response["status"]= status
        return response
    
    @endpoints.route('/get_users',methods=["GET"])
    def get_users():
        resp={}
        try:
            users = user_collection.find({})
            print(users)
            users = list(users)
            status= {
                "statusCode":"200",
                "statusMessage": "Successfully data retrieved"
            }
            output =[{'Name':user['name'],'Email':user['email']} for user in users]
            resp['data']=output
        except Exception as e:
            print(e)
            status= {
                "statusCode":"400",
                "statusMessage": str(e)
            }
        resp['status']=status
        return resp
    
    @endpoints.route('/update-users',methods=["PUT"])
    def update_users():
        resp={}
        try:
            req_body = request.json
            user_collection.update_one({"id":req_body['id']},{"$set":req_body['updated_user_body']})
            print("User Data changed")
            status= {
                "statusCode":"200",
                "statusMessage": "Successfully data updated"
            }
        except Exception as e:
            print(e)
            status= {
                "statusCode":"400",
                "statusMessage": str(e)
            }
        resp['status']=status
        return resp
    @endpoints.route('/delete',methods=['DELETE'])
    def delete():
        resp={}
        try: 
            delete_id = request.args.get('delete_id')
            user_collection.delete_one({"id":delete_id})
            status= {
                "statusCode":"200",
                "statusMessage": "Successfully data deleted"
            }
        except Exception as e:
            print(e)
            status= {
                "statusCode":"400",
                "statusMessage": str(e)
            }
        resp['status']=status
        return resp

    return endpoints
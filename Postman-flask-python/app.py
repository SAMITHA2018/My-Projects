from pathlib import Path 
from flask import Flask,Blueprint, jsonify
from flask_cors import CORS
from flask_pymongo import pymongo

from endpoints import project_api_routes

def my_app():
    Test_app= Flask(__name__)
    CORS(Test_app)

    api_blueprint = Blueprint('api_blueprint',__name__)
    api_blueprint = project_api_routes(api_blueprint)

    Test_app.register_blueprint(api_blueprint,url_prefix='/api')

    return Test_app
app = my_app()
if __name__ == "__main__":
        app.run(host='0.0.0.0',debug=True)
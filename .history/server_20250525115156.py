
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://oo6139116:SzWWT4wcCRputGjU@cluster1.kuekvv6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
app = Flask(__name__)
CORS(app, origins="*")
client = MongoClient(
    uri,
    server_api=ServerApi('1'),
)
@app.route("/")
def home():
    return "Flask App is Running!", 200
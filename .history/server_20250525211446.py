
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
load_dotenv("DB_PASSWORD.env")
db_password = os.getenv("DB_PASSWORD")
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
@app.route("/api/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.json
        myusername = data["username"]
        mypassword = data["password"]

    return jsonify({"ok":True})
if __name__ == "__main__":
    app.run(debug=True,port=8000)
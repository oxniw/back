
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
load_dotenv("DB_PASSWORD.env")
db_password = os.getenv("DB_PASSWORD")
uri = db_password
app = Flask(__name__)
CORS(app, origins="*")
client = MongoClient(
    uri,
    server_api=ServerApi('1'),
)
@app.route("/")
def home():
    return "Flask App is Running!", 200
@app.route("/api/getdata",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        db = client["myfirst"]
        usersdata = db["storedata"]
        user_doc = usersdata.find_one({ "data": { "$exists": True } })
        data = request.json
        print(data)
        
        return jsonify({"message": "Data received", "data": data})

    return jsonify({"ok":True})
if __name__ == "__main__":
    app.run(debug=True,port=8000)
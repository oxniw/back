
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
@app.route("/api/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.json
        myusername = data["username"]
        mypassword = data["password"]
        checkusername = None
        checkusername = usersname.find_one({"username": myusername})
        if checkusername is not None:
            checkpassword = None
            checkpassword = usersnameandpassword.find_one({myusername:mypassword})
            if checkpassword is not None:
                return jsonify({"message":"ok","data":usersdata.find_one({myusername:{"$exists":True}})[myusername],"name":f"{myusername}"})
            else:
                return jsonify({"message":"notok","why":"password incorrect or username incorrect"})
        else:
            return jsonify({"message":"notok","why":"username incorrect"})

    return jsonify({"ok":True})
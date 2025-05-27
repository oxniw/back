
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
        print()
        classes = data.get("class")
        ID = data.get("ID")
        subject = data.get("subject")
        tries = data.get("tries")
        if not classes or not ID or not subject or not tries:
            return jsonify({"error": "Missing required fields"}), 400
        classes = classes.split("/")
        if classes[0] in user_doc["data"]["bigdata"]:
            if classes[1] in user_doc["data"]["bigdata"][classes[0]]:
                if ID in user_doc["data"]["bigdata"][classes[0]][classes[1]]:
                    if subject in user_doc["data"]["bigdata"][classes[0]][classes[1]][ID]:
                        sub:dict = user_doc["data"]["bigdata"][classes[0]][classes[1]][ID][subject]
                        for ject in sub.items():
                            if ject["tries"] == tries:
                                return jsonify({"message": "Data already exists"}), 400
                        #if tries in user_doc["data"]["bigdata"][classes[0]][classes[1]][ID][subject]:
                        #    return jsonify({"message": "Data already exists"}), 400
                        #else:
                        #    return jsonify({"message": "Data received", "data": data}), 200
                    else:
                        return jsonify({"error": "Subject not found"}), 404
                else:
                    return jsonify({"error": "ID not found"}), 404
            else:
                return jsonify({"error": "Class not found"}), 404
        else:
            return jsonify({"error": "Class not found"}), 404

    return jsonify({"ok":True})
if __name__ == "__main__":
    app.run(debug=True,port=8000)
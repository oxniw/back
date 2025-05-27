
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
        ID = data.get("id")
        subject = data.get("subject")
        tries = data.get("tries")
        classes = classes.split("/")
        if classes[0] in user_doc["data"]["bigdata"]:
            print(1)
            if classes[1] in user_doc["data"]["bigdata"][classes[0]]:
                print(2)
                print(ID)
                if ID in user_doc["data"]["bigdata"][classes[0]][classes[1]]:
                    print(3)
        
                    if subject in user_doc["data"]["bigdata"][classes[0]][classes[1]][ID]:
                        print(4)
                        sub:dict = user_doc["data"]["bigdata"][classes[0]][classes[1]][ID][subject]
                        l = len(sub[f"xi {subject}"])
                        check = {}
                        graphtopresent = {}
                        if int(tries) > l:
                            return jsonify({"error": "Tries exceeds available data"}), 400
                        for ject in sub.items():
                            check[ject[0]] = ject[1][int(tries)-1]
                        for ject in sub.items():
                            graphtopresent[ject[0]] = ject[1][0:int(tries)-1]
                        for ject in graphtopresent.items():
                            if len(ject[1]) - 2  >= 0:
                                for i in range(len(ject[1]) - 3):
                                    del graphtopresent[ject[0]][0]
                        print(graphtopresent)
                        print(check)


                                
                        #if len(check) >4:
                        #    for inx,checks in enumerate(check.items()):
                        #        if len(check) - 4 >= inx+1:
                        #            del check[0]
                        return jsonify({"message": "Data already exists","userdata":check}), 200
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
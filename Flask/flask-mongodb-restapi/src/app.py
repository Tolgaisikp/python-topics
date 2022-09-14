from flask import Flask, jsonify, request, Response
from bson import json_util
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/airData"
mongo = PyMongo(app)

@app.route('/users', methods= ['GET'])
def get_airdatasum():
    testData = mongo.db.outsidesummaries.find({},{'_id':0})
    response = json_util.dumps(testData)
    return Response(response, mimetype='application/json')

@app.route('/users/<deviceId>', methods= ['GET'])
def get_device(deviceId):
    testData = mongo.db.outsidesummaries.find({'AA':str(deviceId)},{'AA':1, 'KE':1, 'KB':1, '_id':0})
    response = json_util.dumps(testData)
    return Response(response, mimetype='application/json')

@app.route('/users', methods = ['POST'])
def create_user():
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']

    if username and password and email:
        mongo.db.test.insert_one({'username':username, 'password':password, 'email':email})
        return {'message' : 'received'}
    else:
        return {'message' : 'received'}
        
if __name__ == "__main__":
    app.run(debug=True)
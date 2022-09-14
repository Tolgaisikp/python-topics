from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://localhost:27017") #for docker mongodb://db:27017
db = client['TESTDB']
users = db['Users']

class Register(Resource):
    def post(self):
        postedData = request.json

        username = postedData['username']
        password = postedData['password']

        hashed_pwd = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

        users.insert_one({
            'username': username,
            'password':hashed_pwd, 
            'sentence':'',
            'tokens':10})

        retJson = {
            'status': 200,
            'msg': 'You successfully signed up for the API'
            }

        return jsonify(retJson)

def verifyPw(username, password):
    hashed_pwd = users.find({'username':username})[0]["password"]
    
    if bcrypt.hashpw(password.encode('utf8'), hashed_pwd) == hashed_pwd:
        return True
    else:
        return False

def countTokens(username):
    tokens = users.find({"username":username})[0]["tokens"]
    return tokens

class Store(Resource):
    def post(self):
        postedData = request.json

        username = postedData['username']
        password = postedData['password']
        sentence = postedData['sentence']

        correct_pw = verifyPw(username, password)

        if not correct_pw:
            retJson = {
                'status': 302,
            }
            return jsonify(retJson)

        count_tokens = countTokens(username)
        
        if count_tokens <= 0:
            retJson = {
                "status": 301
            }
            return jsonify(retJson)

        users.update_one({'username':username}, {'$set':{'sentence':sentence, 'tokens':count_tokens-1}})

        retJson = {
            "status":200,
            "msg":"Sentence saved successfully"
        }
        return jsonify(retJson)

class Get(Resource):
    def post(self):
        postedData = request.json
        
        username = postedData['username']
        password = postedData['password']

        correct_pw = verifyPw(username, password)

        if not correct_pw:
            retJson = {
                'status': 302,
            }
            return jsonify(retJson)

        count_tokens = countTokens(username)
        
        if count_tokens <= 0:
            retJson = {
                "status": 301
            }
            return jsonify(retJson)

        sentence = users.find({'username':username})[0]['sentence']

        users.update_one({
            "username":username
        }, {
            "$set":{
                "tokens":count_tokens-1
                }
        })

        retJson = {
            'status':200,
            'sentence':str(sentence)
            }

        return jsonify(retJson)

api.add_resource(Register, '/register')
api.add_resource(Store, '/store')
api.add_resource(Get, '/get')

if __name__ == '__main__':
    app.run(debug=True)







"""app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://localhost:27017") #for docker mongodb://db:27017
db = client['airData']
userNum = db['userNum']

userNum.insert_one({'num_of_users':0})

#Functions
def checkPostedData(postedData, functionName):
    if functionName == 'add' or functionName == 'sub' or functionName == 'mul':
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        else:
            return 200

    elif functionName == 'div':
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        if int(postedData["y"] == 0):
            return 301
        else:
            return 200

#Classes
class Visit(Resource):
    def get(self):
        prev_num = userNum.find({})[0]['num_of_users']
        new_num = prev_num + 1
        userNum.update_one({}, {'$set' :{'num_of_users':new_num}})

        return str('Hello user '+ str(new_num))

class Add(Resource):
    def post(self):
        postedData = request.json

        status_code = checkPostedData(postedData, "add")
        if status_code != 200:
            resJson = {"Message" : "An error happened", 
                       "Status Code": status_code}

            return resJson

        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)
        res = x+y
        resDict = {
            'Message':res,
            'Status Code':200
        }
        return jsonify(resDict)

class Subtract(Resource):
    def post(self):
        postedData = request.json

        status_code = checkPostedData(postedData, "sub")
        if status_code != 200:
            resJson = {"Message" : "An error happened", 
                       "Status Code": status_code}

            return resJson



        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)
        res = x-y
        resDict = {
            'Message':res,
            'Status Code':200
        }
        return jsonify(resDict)

class Multiply(Resource):
    def post(self):
        postedData = request.json

        status_code = checkPostedData(postedData, "mul")
        if status_code != 200:
            resJson = {"Message" : "An error happened", 
                       "Status Code": status_code}

            return resJson



        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)
        res = x*y
        resDict = {
            'Message':res,
            'Status Code':200
        }
        return jsonify(resDict)

class Divide(Resource):
    def post(self):
        postedData = request.json

        status_code = checkPostedData(postedData, "div")
        if status_code != 200:
            resJson = {"Message" : "An error happened", 
                       "Status Code": status_code}

            return resJson



        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)
        res = (x*1.0)/y
        resDict = {
            'Message':res,
            'Status Code':200
        }
        return jsonify(resDict)

api.add_resource(Add, '/add')
api.add_resource(Subtract, '/sub')
api.add_resource(Divide, '/div')
api.add_resource(Multiply, '/mul')
api.add_resource(Visit, '/hello')

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)"""
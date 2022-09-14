from flask import Flask, request, jsonify, g
from flask_restful import Resource, Api
from pymongo import MongoClient
import bcrypt
import spacy

from middleware import hello_middleware

app = Flask(__name__)
api = Api(app)

client = MongoClient('mongodb://db:27017')

db = client['SimilarityDB']
users = db['Users']


def UserExist(username):
    if users.count_documents({'username':username}) == 0:
        return False
    else:
        return True

class Register(Resource):
    def post(self):
        postedData = request.json
        
        username = postedData['username']
        password = postedData['password']

        if UserExist(username):
            retJson = {
                'status':301,
                'msg':'Invalid Username'
            }
            return retJson

        hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        users.insert_one({
            'username':username,
            'password':hashed_pwd,
            'tokens':10})

        retJson = {
            'status':200,
            'msg':"You've successfully signed up to API"
        }

        return retJson


#DETECT
def verifyPw(username, password):
    if not UserExist(username):
        return False

    hashed_pw = users.find({
        "username":username
    })[0]["password"]

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False

def countTokens(username):
    tokens = users.find({
        "username":username
    })[0]["tokens"]
    return tokens

class Detect(Resource):
    def post(self):
        postedData = request.json

        username = postedData['username']
        password = postedData['password']
        text1 = postedData['text1']
        text2 = postedData['text2']

        if  not UserExist(username):
            retJson = {
                "status":301,
                "msg":"Invalid Username"
            }
            return retJson

        correct_pw = verifyPw(username, password)

        if not correct_pw:
            retJson = {
                "status":302,
                "msg": "Incorrect Password"
            }
            return jsonify(retJson)

        num_tokens = countTokens(username)
        
        if num_tokens <= 0:
            retJson = {
                "status": 303,
                "msg": "You are out of tokens, please refill!"
            }
            return jsonify(retJson)

        nlp = spacy.load('en_core_web_sm')
        text1 = nlp(text1)
        text2 = nlp(text2)

        ratio = text1.similarity(text2)

        retJson = {
            "status":200,
            "similarity":ratio,
            "msg": "Similarity score calculated successfully"
        }

        current_tokens = countTokens(username)
        users.update_one({
            "username":username
        }, {
            "$set":{
                "tokens":current_tokens-1
                }
        })

        return jsonify(retJson)


#REFILL
class Refill(Resource):
    def post(self):
        postedData = request.json

        username = postedData['username']
        password = postedData['admin_pwd']
        refill_amount = postedData['refill']

        if UserExist(username):
            retJson = {
                'status':301,
                'msg':'Invalid Username'
            }
            return retJson

        correct_pw = "abc123"
        if not password == correct_pw:
            retJson = {
                "status":304,
                "msg": "Invalid Admin Password"
            }
            return jsonify(retJson)

        current_tokens = countTokens(username)
        users.update_one({
            "username":username
        }, {
            "$set":{
                "tokens":refill_amount + current_tokens
                }
        })

        retJson = {
            "status":200,
            "msg": "Refilled successfully"
        }
        return jsonify(retJson)

api.add_resource(Register, '/register')
api.add_resource(Detect, '/detect')
api.add_resource(Refill, '/refill')

@app.route('/', methods = ['GET'])
@hello_middleware
def hello_world():
    return 'token: {g.token}'

if __name__=="__main__":
    app.run(host='0.0.0.0')
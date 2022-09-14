from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

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

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)
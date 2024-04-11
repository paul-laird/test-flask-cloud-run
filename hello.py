from flask import Flask
from flask import request
from flask_cors import CORS
import json
import requests
app = Flask(__name__)
CORS(app)


@app.route("/") #Default - Show Data
def hello(): # Name of the method
  Results=[{"Name":"Paul","Email":"test1@test.ie","ID":1},{"Name":"John","Email":"test2@test.ie","ID":2}]    
  response={'Results':Results, 'count':len(Results)}
  ret=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )
  return ret #Return the data in a string format




@app.route("/hello")
def hello():
    return "Hello once again from Dockerised Flask"

@app.route("/route32a")
def route32a():
    return "Hello from the 32A"

@app.route("/route")
def route():
    number=requests.get('number')
    return "Hello from the {}".format(number)



if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')

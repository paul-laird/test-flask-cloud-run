from flask_cors import CORS
from flask import Flask
import requests
from flask import request
from flask import render_template
import json
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    r= '''{"Results":[{"Name":"Paul","Email":"test1@test.ie","ID":1},{"Name":"John","Email":"test2@test.ie","ID":2}],
      "count":2}'''
    ret=app.response_class(
      response=r,
      status=200,
      mimetype='application/json'
    )
    return ret

@app.route("/route32a")
def route32a():
    return "Hello from the 32A"

@app.route("/new")
def newRoute():
    return "This is a new route"

@app.route("/user/<identity>") # PS THIS IS COMPLETELY FAKE
def identity(identity):
    identity=int(identity)
    r= json.loads('''{"Results":[{"Name":"Paul","Email":"test1@test.ie","ID":1},{"Name":"John","Email":"test2@test.ie","ID":2}],
      "count":2}''')
    r['Results']=list(filter(lambda x:x['ID']==identity,r['Results']))
    r['count']=len(r['Results'])
    r=json.dumps(r)
    ret=app.response_class(
      response=r,
      status=200,
      mimetype='application/json'
    )
    return ret

@app.route("/index.html")
def index():

    return render_template('index.html')

@app.route("/route")
def route():
    number=request.args.get('number')
    return "Hello from the {}".format(number)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')

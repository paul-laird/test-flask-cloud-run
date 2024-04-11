from flask import Flask
import requests
app = Flask(__name__)

@app.route("/")
def hello():
    return '''{"Result":[{"Name":"Paul","Email":"test1@test.ie","ID":1},{"Name":"John","Email":"test2@test.ie","ID":2}],
      "count":2}'''

@app.route("/route32a")
def route32a():
    return "Hello from the 32A"

@app.route("/new")
def newRoute():
    return "This is a new route"

@app.route("/route")
def route():
    number=requests.get('number')
    return "Hello from the {}".format(number)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')

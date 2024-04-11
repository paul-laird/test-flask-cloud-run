from flask import Flask
import requests
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello again from Dockerised Flask"

@app.route("/route32a")
def route32a():
    return "Hello from the 32A"

@app.route("/route")
def route():
    number=requests.get('number')
    return "Hello from the {}".format(number)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')

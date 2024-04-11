from flask import Flask
from flask import request
from flask_cors import CORS
import json
import requests
app = Flask(__name__)
CORS(app)


@app.route("/") #Default - Show Data
def hello(): # Name of the method
    
  a='''cur = mysql.connection.cursor() #create a connection to the SQL instance
  rv = cur.fetchall() #Retreive all rows returend by the SQL statment
  Results=[]
  for row in rv: #Format the Output Results and add to return string
    Result={}
    Result['Name']=row[0].replace('\n',' ')
    Result['Email']=row[1]
    Result['ID']=row[2]
    Results.append(Result)

    '''
  Results=[{"Name":"Paul","Email":"test1@test.ie","ID":1},{"Name":"John","Email":"test2@test.ie","ID":2}]
    
  response={'Results':Results, 'count':len(Results)}
  ret=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )
  return ret #Return the data in a string format




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

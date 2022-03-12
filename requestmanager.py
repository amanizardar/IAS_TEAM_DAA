from flask import Flask, request, render_template
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/signup', methods = ['GET', 'POST'])
def signin():
    data = request.get_json()
    print("data got = ",data)
    response=requests.post('http://localhost:1235/add_user',json=data).content
    return "ok"


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if(request.method=='POST'): 
        data = request.get_json()
        response=requests.post('http://localhost:1235/authen',json=data).content.decode()
        if(response=="ok"):
            return "ok"
        else:
            return "Error"




if(__name__ == '__main__'):
    app.run(port=1234,debug=True)

from aiohttp import request
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/signin', methods = ['GET', 'POST'])
def signin():
    pass


@app.route('/login', methods = ['GET', 'POST'])
def login():
    data = request.get_json()
    response=requests.post('http://localhost:1235/authen',json=to_send).content
    if(response=="ok"):
        return True
    else:
        return False




if(__name__ == '__main__'):
    app.run(port=1234,debug=True)

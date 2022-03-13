from flask import Flask, request, render_template
from flask import Flask
from authentication import User_AD, User_DS
import requests
import cgi, os
import json
import jwt
import cgitb; cgitb.enable()
from werkzeug.utils import secure_filename

usename ="user"
password="admin"

app = Flask(__name__)
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/role',methods = ['POST', 'GET'])
def role():
    if (request.method == 'POST'):
        rol = request.form['role']
        if(rol=='Data Scientist'):

          return render_template('dem.html')
        else:
            return render_template('dema.html')

def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

@app.route('/signup_DS', methods = ['GET', 'POST'])
def signin():
    username=request.form['username']
    password=request.form['password']
    # data = request.get_json()
    # print("data got = ",data)
    response=requests.post('http://localhost:5000/add_user_DS',json={'username':username,'password':password}).content.decode()
    payload = json.loads(response)
    if(payload["message"]=="ok"):
        to_send={}
        to_send["username"]=username
        response=requests.post('http://localhost:1237/get_models',json=to_send).content
        response =response.decode().split()

        return render_template("Dashboard.html",response=response)
    else:
        return "Error"
    


@app.route('/login_DS', methods = ['GET', 'POST'])
def login():
    if(request.method=='POST'): 
        username=request.form['username']
        password=request.form['password']
        # data = request.get_json()
        response=requests.post('http://localhost:5000/authen_DS',json={'username':username,'password':password}).content.decode()
        payload = json.loads(response)
        if(payload["message"]=="ok"):
            to_send={}
            to_send["username"]=username
            response=requests.post('http://localhost:1237/get_models',json=to_send).content
            response =response.decode().split()
            return render_template("Dashboard.html",response=response)
        else:
            return "Error"

@app.route('/signup_AD', methods = ['GET', 'POST'])
def signup():
    # data = request.get_json()
    username=request.form['username']
    password=request.form['password']
    # print("data got = ",data)
    response=requests.post('http://localhost:5000/add_user_AD',json={'username':username,'password':password}).content.decode()
    payload = json.loads(response)
    if(payload["message"]=="ok"):
            to_send={}
            to_send["username"]=username
            response=requests.post('http://localhost:1237/get_apps',json=to_send).content
            response =response.decode().split()
            return render_template("Dashboard.html",response=response)
    else:
        return "Error"


@app.route('/login_AD', methods = ['GET', 'POST'])
def logup():
    if(request.method=='POST'): 
        # data = request.get_json()
        username=request.form['username']
        password=request.form['password']
        response=requests.post('http://localhost:5000/authen_AD',json={'username':username,'password':password}).content.decode()
        payload = json.loads(response)
        if(payload["message"]=="ok"):
            to_send={}
            to_send["username"]=username
            response=requests.post('http://localhost:1237/get_apps',json=to_send).content
            response =response.decode().split()
            return render_template("Dashboard.html",response=response)
        else:
            return "Error"

@app.route('/Upload', methods = ['GET', 'POST'])
def upload():
    if(request.method=='POST'): 
        
        # Send this request to Scheduler

        

        # Just maintaining a copy here.

        # app.config['UPLOAD_FOLDER'] = "./Data/Model/"

        to_send={}

        global username
        

        #########################
        #########Authentication Check
        # auth_header = request.headers.get('Authorization')
        # if auth_header:
        #     auth_token = auth_header.split(" ")[1]
        # else:
        #     auth_token = ''
        # if auth_token:
        # resp = decode_auth_token(auth_token)
        # if not isinstance(resp, str):
        ##########################
        f = request.files['filename']
        f.save(os.path.join("./Data/Model/", f.filename))

        to_send["username"]=username
        to_send["model_name"]=f.filename
        response=requests.post('http://localhost:1237/add_model',json=to_send).content.decode()
        if(response.decode()=="ok"):
            return "Model uploaded"
        else:
            return "error"


        print(f)
        print(f.filename)



        # f.save(secure_filename(f.filename))

        
        # form = cgi.FieldStorage()
        # this_fileitem = form['filename']
        # if f.filename:
        #     fn = os.path.basename(f.filename)
        #     open('./Data/Model/' + fn, 'w').write(f.file.read())
        #     message = 'The file "' + fn + '" was uploaded successfully'
        # else:
        #     message = 'No file was uploaded'
    
        # print(message)
        return "KK"

if(__name__ == '__main__'):
    app.run(port=8080,debug=True)

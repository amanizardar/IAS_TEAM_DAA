from flask import Flask, session, request, render_template, redirect
from authentication import User_AD, User_DS
import requests
import cgi, os
import json
import jwt
import cgitb; cgitb.enable()
from werkzeug.utils import secure_filename
from flask_session import Session

usename ="user"
password="admin"


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
# session["auth_token"] = ''
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/role',methods = ['POST', 'GET'])
def role():
    if (request.method == 'POST'):
        rol = request.form['role']
        if(rol=='Data Scientist'):
            return render_template('dem.html',authcode="None",mesg="")
        else:
            return render_template('dema.html',authcode="None",mesg="")

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
        to_send["username"] = username
        session["auth_token"] = payload["auth_token"]
        response=requests.post('http://localhost:1237/get_models',json=to_send).content
        response =response.decode().split()

        return render_template("Dashboard.html",response=response)
    else:
        return render_template('dem.html',authcode="error_signup",mesg=payload["message"])
    


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
            session["auth_token"] = payload["auth_token"]
            response=requests.post('http://localhost:1237/get_models',json=to_send).content
            response =response.decode().split()
            return render_template("Dashboard.html",response=response,authcode=None)
        else:
            return render_template('dem.html',authcode="error_login",mesg=payload["message"])

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
            session["auth_token"] = payload["auth_token"]
            response=requests.post('http://localhost:1237/get_apps',json=to_send).content
            response =response.decode().split()
            return render_template("Dashboard.html",response=response)
    else:
         return render_template('dem.html',authcode="error_signup",mesg=payload["message"])


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
            session["auth_token"] = payload["auth_token"]
            response=requests.post('http://localhost:1237/get_apps',json=to_send).content
            response =response.decode().split()
            return render_template("Dashboard.html",response=response)
        else:
            return render_template('dem.html',authcode="error_login",mesg=payload["message"])


@app.route("/logout", methods = ['GET', 'POST'])
def logout():
    session["auth_token"] = None
    return redirect("/")

@app.route('/Upload_DS', methods = ['GET', 'POST'])
def uploadds():
    if(request.method=='POST'): 

        # Send this request to Scheduler

        

        # Just maintaining a copy here.

        # app.config['UPLOAD_FOLDER'] = "./Data/Model/"

        to_send={}

        # global username
        username = request.form["username"]
       
        if  session["auth_token"] :
            resp = decode_auth_token( session["auth_token"] )
            if not isinstance(resp, str):
                f = request.files['filename']
                f.save(os.path.join("./Data/Model/", f.filename))
                to_send["username"]=username
                to_send["model_name"]=f.filename
                response=requests.post('http://localhost:1237/add_model',json=to_send).content
                if(response.decode()=="ok"):
                    return "Model uploaded"
                else:
                    return "error"
                print(f)
                print(f.filename)
                return "KK"
        else:
            return "error"

@app.route('/Upload_AD', methods = ['GET', 'POST'])
def uploadad():
    if(request.method=='POST'): 

        # Send this request to Scheduler

        

        # Just maintaining a copy here.

        # app.config['UPLOAD_FOLDER'] = "./Data/Model/"

        to_send={}

        # global username
        
        username = request.form["username"]
        if  session["auth_token"] :
            resp = decode_auth_token( session["auth_token"] )
            if not isinstance(resp, str):
                f = request.files['filename']
                f.save(os.path.join("./Data/App/", f.filename))

                to_send["username"]=username
                to_send["app_name"]=f.filename
                response=requests.post('http://localhost:1237/add_app',json=to_send).content
                if(response.decode()=="ok"):
                    return "app uploaded"
                else:
                    return "error"
        else:
            return "error"



if(__name__ == '__main__'):
    app.run(port=8080,debug=True)

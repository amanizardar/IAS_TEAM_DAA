from flask import Flask, request, render_template
from flask import Flask
import requests
import cgi, os
import cgitb; cgitb.enable()
from werkzeug.utils import secure_filename

# username ="user"
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


@app.route('/signup_DS', methods = ['GET', 'POST'])
def signin():
    username=request.form['username']
    password=request.form['password']
    # data = request.get_json()
    # print("data got = ",data)
    response=requests.post('http://localhost:5000/add_user_DS',json={'username':username,'password':password}).content
    if(response.decode()=="ok"):
        to_send={}
        to_send["username"]=username
        response=requests.post('http://localhost:1237/get_models',json=to_send).content
        response =response.decode().split()

        return render_template("Dashboard.html",response=response,username=username)
    else:
        return "Error"
    


@app.route('/login_DS', methods = ['GET', 'POST'])
def login():
    if(request.method=='POST'): 
        username=request.form['username']
        password=request.form['password']
        # data = request.get_json()
        response=requests.post('http://localhost:5000/authen_DS',json={'username':username,'password':password}).content.decode()
        if(response=="ok"):
            to_send={}
            to_send["username"]=username
            response=requests.post('http://localhost:1237/get_models',json=to_send).content
            response =response.decode().split()
            return render_template("Dashboard.html",response=response,username=username)
        else:
            return "Error"

@app.route('/signup_AD', methods = ['GET', 'POST'])
def signup():
    # data = request.get_json()
    username=request.form['username']
    password=request.form['password']
    # print("data got = ",data)
    response=requests.post('http://localhost:5000/add_user_AD',json={'username':username,'password':password}).content
    if(response.decode()=="ok"):
            to_send={}
            to_send["username"]=username
            response=requests.post('http://localhost:1237/get_apps',json=to_send).content
            response =response.decode().split()
            response2=requests.post('http://localhost:1237/get_all_models',json=to_send).content.decode().split()

            return render_template("Dashboard1.html",response=response,response2=response2,username=username)
    else:
        return "Error"


@app.route('/login_AD', methods = ['GET', 'POST'])
def logup():
    if(request.method=='POST'): 
        # data = request.get_json()
        username=request.form['username']
        password=request.form['password']
        response=requests.post('http://localhost:5000/authen_AD',json={'username':username,'password':password}).content.decode()
        if(response=="ok"):
            to_send={}
            to_send["username"]=username
            response=requests.post('http://localhost:1237/get_apps',json=to_send).content
            response =response.decode().split()
            response2=requests.post('http://localhost:1237/get_all_models',json=to_send).content.decode().split()
            return render_template("Dashboard1.html",response=response,response2=response2,username=username)
        else:
            return "Error"

@app.route('/Upload_DS', methods = ['GET', 'POST'])
def uploadds():
    if(request.method=='POST'): 

        # Send this request to Scheduler

        

        # Just maintaining a copy here.

        # app.config['UPLOAD_FOLDER'] = "./Data/Model/"

        to_send={}

        # global username
        username = request.form["username"]
        # print("username is ",user)
        

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

@app.route('/Upload_AD', methods = ['GET', 'POST'])
def uploadad():
    if(request.method=='POST'): 

        # Send this request to Scheduler

        

        # Just maintaining a copy here.

        # app.config['UPLOAD_FOLDER'] = "./Data/Model/"

        to_send={}

        # global username
        
        username = request.form["username"]

        f = request.files['filename']
        f.save(os.path.join("./Data/App/", f.filename))

        to_send["username"]=username
        to_send["app_name"]=f.filename
        response=requests.post('http://localhost:1237/add_app',json=to_send).content
        if(response.decode()=="ok"):
            return "app uploaded"
        else:
            return "error"


  



if(__name__ == '__main__'):
    app.run(port=8080,debug=True)

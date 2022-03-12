from flask import Flask, request, render_template
from flask import Flask
import requests
import cgi, os
import cgitb; cgitb.enable()
from werkzeug.utils import secure_filename


app = Flask(__name__)


@app.route('/signup_DS', methods = ['GET', 'POST'])
def signin():
    data = request.get_json()
    print("data got = ",data)
    response=requests.post('http://localhost:1235/add_user_DS',json=data).content
    return "ok"


@app.route('/login_DS', methods = ['GET', 'POST'])
def login():
    if(request.method=='POST'): 
        data = request.get_json()
        response=requests.post('http://localhost:1235/authen_DS',json=data).content.decode()
        if(response=="ok"):
            return "ok"
        else:
            return "Error"

@app.route('/signup_AD', methods = ['GET', 'POST'])
def signin():
    data = request.get_json()
    print("data got = ",data)
    response=requests.post('http://localhost:1235/add_user_AD',json=data).content
    return "ok"


@app.route('/login_AD', methods = ['GET', 'POST'])
def login():
    if(request.method=='POST'): 
        data = request.get_json()
        response=requests.post('http://localhost:1235/authen_AD',json=data).content.decode()
        if(response=="ok"):
            return "ok"
        else:
            return "Error"

@app.route('/Upload', methods = ['GET', 'POST'])
def upload():
    if(request.method=='POST'): 

        # Send this request to Scheduler

        

        # Just maintaining a copy here.

        # app.config['UPLOAD_FOLDER'] = "./Data/Model/"
        f = request.files['filename']
        print(f)
        print(f.filename)
        f.save(os.path.join("./Data/Model/", f.filename))
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
    app.run(port=1234,debug=True)

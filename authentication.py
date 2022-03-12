from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager, login_user, logout_user, login_required, UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = 'secretkey'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class User_DS(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

class User_AD(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)




@app.route('/add_user_DS', methods = ['GET', 'POST'])
def do_signup():
    if(request.method=='POST'):
        data=request.get_json()
        username = data['username']
        password = data['password']
        print("username is ",username)
        print("Password is ",password)
        check_user = User_DS.query.filter_by(username=username).first()
        if(check_user is not None):
            return "User already registered, please sign in"
        else:
            user = User_DS(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return "Registered Successfully"

@app.route('/authen_DS', methods = ['GET', 'POST'])
def authen():
    if(request.method=='POST'):
        data=request.get_json()
        username = data['username']
        password = data['password']
        check_user = User_DS.query.filter_by(username=username).first()
        if(check_user is not None):
            if(check_user.password == password):
                login_user(check_user)
                return "ok"
            else:
                return "Incorrect Password"
        else:
            return "No such User exists"

@app.route('/add_user_AD', methods = ['GET', 'POST'])
def do_signup():
    if(request.method=='POST'):
        data=request.get_json()
        username = data['username']
        password = data['password']
        print("username is ",username)
        print("Password is ",password)
        check_user = User_AD.query.filter_by(username=username).first()
        if(check_user is not None):
            return "User already registered, please sign in"
        else:
            user = User_AD(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return "Registered Successfully"

@app.route('/authen_AD', methods = ['GET', 'POST'])
def authen():
    if(request.method=='POST'):
        data=request.get_json()
        username = data['username']
        password = data['password']
        check_user = User_AD.query.filter_by(username=username).first()
        if(check_user is not None):
            if(check_user.password == password):
                login_user(check_user)
                return "ok"
            else:
                return "Incorrect Password"
        else:
            return "No such User exists"



if(__name__ == '__main__'):
    app.run(port=1235,debug=True)
    db.create_all()

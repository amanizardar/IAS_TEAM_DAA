from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager, login_user, logout_user, login_required, UserMixin
import requests


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///User.db'
app.config['SECRET_KEY'] = 'secretkey'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(80), nullable=False)



class User_DS(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

class User_AD(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


# class model(UserMixin,db.Model):
#     # id = db.Column(db.Integer, primary_key = True)
#     __tablename__='model'
#     # id=db.Column(db.Integer,unique = True,autoincrement=True)
#     username = db.Column(db.String(100),primary_key = True,unique = True)
#     password = db.Column(db.String(100))
#     loginornot=db.Column(db.Integer,default=0)
 
 
#     def __init__(self, username, password,loginornot):
#         self.username = username
#         self.password = password
#         self.loginornot=loginornot
        
#     def get_id(self):
#         print("Get id called")
#         # print(self.id)
#         return self.username


@login_manager.user_loader
def load_user (user_id):
    print("hi inside the userloader")
    print(user_id)
    return User_AD.query.get(user_id)

# @app.route('/')
# def home():
#    return render_template('index.html')



# @app.route('/role',methods = ['POST', 'GET'])
# def role():
#     if (request.method == 'POST'):
#         rol = request.form['role']
#         if(rol=='Data Scientist'):

#           return render_template('dem.html')
          
#           user=input("Please Enter Your Username: ")
#           password=(input("Enter Password: "))
#           if(isvalid(user,password)):
#               username=user
#               do_operations()
#           else:
#               print("Please Try again Username or password is not valid")
    
#         else:
#             return render_template('dema.html')


# @app.route('/add_user', methods = ['GET', 'POST'])
# def do_signup():
#     if(request.method=='POST'):
#         data=request.get_json()
#         username = data['username']
#         password = data['password']
#         print("username is ",username)
#         print("Password is ",password)
#         check_user = User.query.filter_by(username=username).first()
#         if(check_user is not None):
#             return "User already registered, please sign in"
#         else:
#             user = User(username=username, password=password)
#             db.session.add(user)
#             db.session.commit()
#             return "Registered Successfully"

# @app.route('/authen', methods = ['GET', 'POST'])
# def authen():
#     if(request.method=='POST'):
#         data=request.get_json()
#         username = data['username']
#         password = data['password']
#         check_user = User.query.filter_by(username=username).first()
#         if(check_user is not None):
#             if(check_user.password == password):
#                 login_user(check_user)
#                 return "ok"
#             else:
#                 return "Incorrect Password"
#         else:
#             return "No such User exists"












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
            return "ok"

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
def do_signupad():
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
            return "ok"

@app.route('/authen_AD', methods = ['GET', 'POST'])
def authenad():
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
    app.run(port=5000,debug=True)
    db.create_all()

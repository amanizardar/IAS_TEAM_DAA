from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager, login_user, logout_user, login_required, UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = 'secretkey'

db = SQLAlchemy(app)
# login_manager = LoginManager()
# login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)



@app.route('/add_user', methods = ['GET', 'POST'])
def do_signup():
    if(request.method=='POST'):
        username = request.form['username']
        password = request.form['password']
        check_user = User.query.filter_by(username=username).first()
        if(check_user is not None):
            return "User already registered, please sign in"
        else:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return "Registered Successfully"

@app.route('/authen', methods = ['GET', 'POST'])
def authen():
    if(request.method=='POST'):
        username = request.form['username']
        password = request.form['password']
        check_user = User.query.filter_by(username=username).first()
        if(check_user is not None):
            if(check_user.password == password):
                login_user(check_user)
                return "LOGGED in successfully"
            else:
                return "Incorrect Password"
        else:
            return "No such User exists"



if(__name__ == '__main__'):
    app.run(port=1235,debug=True)
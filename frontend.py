import requests
import json

print("Welcome To The AI PLATFORM")
print("Please Login To continue")
print("Press 1 for Login, 2 For SignUp, and 3 for Exit")

username="xyz"

def do_operations():
    pass

def isvalid(username,password):
    to_send={}
    to_send["username"]=username
    to_send["password"]=password
    response=requests.post('http://localhost:1234/login',json=to_send).content
    if(response=="ok"):
        return True
    else:
        return False

def signup(username,password):
    to_send={}
    to_send["username"]=username
    to_send["password"]=password
    response=requests.post('http://localhost:1234/signup',json=to_send).content
    return


opt = int(input)
if(opt==1):
    # Login
    user=input("Please Enter Your Username")
    password=(input("Enter Password"))
    if(isvalid(user,password)):
        username=user
        do_operations()

elif(opt==2):
    # SignUp
    user=input("Please Enter Your Username")
    password=(input("Enter Password"))
    signup(user,password)
    username=user
    do_operations()


else:
    exit()
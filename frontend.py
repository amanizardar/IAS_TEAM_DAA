import requests
import json



username="xyz"

def do_operations():
    print("you are inside do_operation method")

def isvalid(username,password):
    to_send={}
    to_send["username"]=username
    to_send["password"]=password
    response=requests.post('http://localhost:1234/login',json=to_send).content.decode()
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



print("Welcome To The AI PLATFORM")
print("Please Login To continue")
print("Press 1 for Login, 2 For SignUp, and 3 for Exit")

opt = int(input())
if(opt==1):
    # Login
    user=input("Please Enter Your Username: ")
    password=(input("Enter Password: "))
    if(isvalid(user,password)):
        username=user
        do_operations()
    else:
        print("Please Try again Username or password is not valid")

elif(opt==2):
    # SignUp
    user=input("Please Enter Your Username: ")
    password=(input("Enter Password: "))
    signup(user,password)
    username=user
    do_operations()


else:
    exit()
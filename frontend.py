from distutils.command.config import config
import requests
import json
import socket



username="xyz"

def handle_data_scientist():
    pass

def handle_app_developer():
    pass

def download_config():
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("127.0.0.1",1236))

    with open("config.json") as f:
        while 1:
            data = s.recv(1024)

            if not data:
                break
            f.write(data)
    s.close()
    print("Config_file",'successfully downloaded.')

def do_operations():
    print("you are inside do_operation method")
    print("Press 1 if you are Want to deploy your AI model")
    print("Press 2 if you are Want to deploy your Application")
    print("Press 3 To Download Platform Config File")
    print("Press 4 to exit")

    opt = int(input())

    if(opt==1):
    # Data_Scientist handle
        handle_data_scientist()
        

    elif(opt==2):
        # App developer
        handle_app_developer()

    elif(opt==3):
        download_config()

    elif(opt==4):
        exit()
    else:
        print("Error Please Try again!")






    

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
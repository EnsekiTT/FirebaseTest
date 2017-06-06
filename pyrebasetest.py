import pyrebase
import json

with open('config.json', 'r') as f:
    config = json.load(f)
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
db = firebase.database()

def create(auth):
    email = "hogehoge1@example.com"
    password = "set your password"
    result = auth.create_user_with_email_and_password(email, password)
    print(result)

def read(auth):
    email = "hogehoge1@example.com"
    password = "set your password"
    user = auth.sign_in_with_email_and_password(email, password)
    print(json.dumps(user, indent=2))
    return user

#create(auth)
user = read(auth)
data = {"name": "hogehoge manju maru"}

result = db.child("users").push(data,user['idToken'])
print(json.dumps(result, indent=2))
input()
result = db.child("users").remove(user['idToken'])
print(result)

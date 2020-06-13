import pyrebase
from flask import Flask, request
from flask_restful import Resource, Api

config = {
    "apiKey": "AIzaSyAgLJEAk3vGgql5jsDpZi-aQgOsd03Fto0",
    "authDomain": "munchkin-55db1.firebaseapp.com",
    "databaseURL": "https://munchkin-55db1.firebaseio.com",
    "projectId": "munchkin-55db1",
    "storageBucket": "munchkin-55db1.appspot.com",
    "messagingSenderId": "118394564063",
    "appId": "1:118394564063:web:2b0fc5c316bb726815286a",
    "measurementId": "G-XVKT8244CK"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
app = Flask(__name__)
api = Api(app)

class Players(Resource):
    def get(self):
        pass

api.add_resource(Players, '/players')

@app.route('/', methods=['GET','POST'])

def basic():
    return 'Welcome!'

if __name__ == '__main__':
    app.run(port=5002)

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Players(Resource):
    def get(self):
        pass

api.add_resource(Players, '/players')

if __name__ == '__main__':
    app.run(port=5002)
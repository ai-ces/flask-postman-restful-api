from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

class Class(Resource):
    def post(self):
        try:
            username = request.args.get("username")
            password = request.args.get("pass")
            print(username,password)

        except Exception as e:
            return e
        

api.add_resource(Class,"/try")

if __name__ == "__main__":
    app.run()
    print(app.logger.error)
from flask import Flask
from flask_restful import Api
from resources.user import UserRegister
from resources.user import UserLogin
from resources.usertest import UserTest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'praheja'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(UserRegister, '/register')
api.add_resource(UserTest, '/checkuser')
api.add_resource(UserLogin, '/login')
from db import db
db.init_app(app)
if __name__ == '__main__':

    app.run(port=5000, debug=True)
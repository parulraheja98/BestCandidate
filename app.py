from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.user import UserRegister,UserLogin
from resources.skills import SkillFinder
from models.user import UserModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'praheja'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWTManager(app)

@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    admin_user = UserModel.find_by_role('admin').json()['id']
    if identity == admin_user:
        return {'is_admin': True}
    else:
        return {'is_admin': False}


api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(SkillFinder,'/skill')
from db import db
db.init_app(app)
if __name__ == '__main__':

    app.run(port=5000, debug=True)
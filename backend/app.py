from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from resources.user import UserRegister,UserLogin, UserLogout, JobsAppliedByCandidate
from resources.skills import SkillFinder
from resources.job import Job, CreateJob, CandidatesByJob, ListJobs
from resources.recruiter import Recruiter,CreateRecruiter, RecruiterLogin, ListRecruiters
from resources.application import Application, CreateApplication, ListApplications, ApplicationByCandidate, ListCandidatesByJob
from models.user import UserModel
from blacklist import BLACKLIST


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://praheja:parulraheja@35.226.222.111/praheja'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.secret_key = 'praheja'
api = Api(app)
CORS(app, origins="http://localhost:3000", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
    supports_credentials=True)



@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWTManager(app)

@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    print('identity check')
    print(identity)
    admin_user = UserModel.find_by_role('admin')
    list_of_admin = []
    for user in admin_user:

        if user.json()['role'] == 'admin':
            list_of_admin.append(user.json()['id'])

    if identity in list_of_admin:
        return {'is_admin': True, 'identity': identity}
    else:
        return {'is_admin': False, 'identity': identity}

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token['jti'] in BLACKLIST

@jwt.expired_token_loader
def expired_token_callback(error):
    return jsonify({
        'message': 'This token has expired',
        'error': 'invalid_token'
    }), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'message': 'Request doesnot contain access token',
        'error': 'authorization_required'
    }), 401

@jwt.needs_fresh_token_loader
def token_not_fresh_callback(error):
    return jsonify({
        'description': 'the token is not fresh',
        'error': 'fresh_token_required'
    }), 401

@jwt.revoked_token_loader
def revoked_token_callback(error):
    return jsonify({
        'description': 'The token has been revoked',
        'error': 'token_revoked'
    }), 401


api.add_resource(UserRegister, '/candidates')
api.add_resource(UserLogin, '/candidates/login')
api.add_resource(RecruiterLogin, '/recruiters/login')
api.add_resource(SkillFinder, '/skill')
api.add_resource(UserLogout, '/logout')
api.add_resource(Job, '/jobs/<int:id>')
api.add_resource(ListJobs,'/jobs')
api.add_resource(CreateJob,'/jobs')
api.add_resource(Recruiter, '/recruiters/<int:id>')
api.add_resource(CreateRecruiter,'/recruiters')
api.add_resource(ListRecruiters,'/recruiters')
api.add_resource(CreateApplication,'/applications')
api.add_resource(ListApplications,'/applications')
api.add_resource(Application, '/applications/<int:id>')
api.add_resource(JobsAppliedByCandidate,'/candidates/<int:id>/jobs')
api.add_resource(CandidatesByJob,'/jobs/<int:id>/candidates')

from db import db
db.init_app(app)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

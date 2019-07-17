import hashlib
from models.recruiter import RecruiterModel
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_claims, jwt_refresh_token_required, get_raw_jwt


class Recruiter(Resource):
    def get(self, id):
        recruiter = RecruiterModel.find_by_id(id)
        if recruiter != None:
            return recruiter.json(),200
        else:
            return {"error": "Recruiter Not Found"},404

class CreateRecruiter(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'username',
            type=str,
            required=True,
            help="Username field is required"
        )
        parser.add_argument(
            'password',
            type=str,
            required=True,
            help="Password field is required"
        )
        parser.add_argument(
            'firstname',
            type=str,
            required=True,
            help="First Name field is required"
        )
        parser.add_argument(
            'lastname',
            type=str,
            required=True,
            help="Last Name field is required"
        )
        parser.add_argument(
            'title',
            type=str,
            required=True,
            help="Title field is required"
        )
        parser.add_argument(
            'company',
            type=str,
            required=True,
            help="Company field is required"
        )
        data = parser.parse_args()
        if RecruiterModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400
        recruiter_username = data['username']

        enc_password = hashlib.md5(data['password'].encode())
        firstname = data['firstname']
        lastname = data['lastname']
        recruiter_title = data['title']
        recruiter_company = data['company']

        recruiter = RecruiterModel(recruiter_username,enc_password.hexdigest(),firstname,lastname,recruiter_title, recruiter_company)
        recruiter.save_to_db()

        return {
            'message': 'Recruiter successfully created'
        }, 200
        

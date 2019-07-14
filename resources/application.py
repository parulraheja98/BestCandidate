from models.application import ApplicationModel
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_claims, jwt_refresh_token_required, get_raw_jwt


class Application(Resource):
    def get(self, id):
        application = ApplicationModel.find_by_id(id).json()
        print(application)
        job = application['job']
        candidate = application['candidate']
        return {
            'job': job,
            'candidate': candidate
        }, 200

class ApplicationByCandidate(Resource):
    def get(self, id):
        application = ApplicationModel.find_by_candidate(id)
        pos_list_id = []
        for appl in application:
            print(pos.json())

        return application

class CreateApplication(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'job',
            type=str,
            required=True,
            help="This field cannot be blank"
        )
        parser.add_argument(
            'user',
            type=int,
            required=True,
            help="This field cannot be blank"
        )
        data = parser.parse_args()
        application_job = data['job']
        application_candidate = data['user']

        job = ApplicationModel(application_job, application_candidate)
        job.save_to_db()
       





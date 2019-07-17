from models.application import ApplicationModel
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_claims, jwt_refresh_token_required, get_raw_jwt
from models.job import JobModel
from models.user import UserModel

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
    @jwt_required
    def get(self, id):
        claims = get_jwt_claims()
        print(claims)
        application = ApplicationModel.find_by_candidate(id)
        job_list_id = []
        for appl in application:
            job_list_id.append(appl.json()['job'])
        jobs_applied = []
        for list_of_jobs in job_list_id:
            job_list = JobModel.find_by_id(list_of_jobs).json()
            jobs_applied.append(job_list)
            
        return jobs_applied

class ListCandidatesByJob(Resource):
    def get(self, id):
        application = ApplicationModel.find_by_job(id)
        candidate_list_id = []
        for appl in application:
            candidate_list_id.append(appl.json()['candidate'])
        candidates_applied = []
        for id in candidate_list_id:
            candidate = UserModel.find_by_id(id).json()
            candidates_applied.append(candidate)

        return candidates_applied


class CreateApplication(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'job',
            type=int,
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

        return {'message': 'Application Created Successfully '}, 200
       





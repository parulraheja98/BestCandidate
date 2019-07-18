from models.job import JobModel
from models.application import ApplicationModel
from models.user import UserModel
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_claims, jwt_refresh_token_required, get_raw_jwt
from datetime import datetime
import json
from bson import json_util

class Job(Resource):
    def get(self, id):
        print("id is " + str(id))
        job = JobModel.find_by_id(id)
        if job != None:
            job_details = json.dumps(job.json(), indent=1, sort_keys=True, default=str)
            job_details_res = json.loads(job_details)
            return job_details_res,200
        else:
            return {"error": "Job Not Found"},404

class ListJobs(Resource):
    def get(self):
        jobs = JobModel.find_all()
        list_of_jobs = []
        for job in jobs:
            job_details = json.dumps(job.json(), indent=1, sort_keys=True, default=str)
            list_of_jobs.append(json.loads(job_details))
            
        return list_of_jobs

class CandidatesByJob(Resource):
    @jwt_required
    def get(self, id):
        claims = get_jwt_claims()
        id_recruiter = claims['identity']
        jobs = JobModel.find_by_posted_by(id_recruiter)
        id_exists = False
        for job in jobs:
            if job.json()['id'] == id:
                id_exists = True

        if id_exists:
            application = ApplicationModel.find_by_job(id)
            candidate_list_id = []
            for appl in application:
                candidate_list_id.append(appl.json()['candidate'])
            candidates_applied = []
            for id in candidate_list_id:
                candidate = UserModel.find_by_id(id).json()
                candidates_applied.append(candidate)
            return candidates_applied
        else:
            return {
                'message': 'Job Not Associated with the recruiter',
                'error': 'unauthorized_access'
            }, 401

class CreateJob(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'title',
            type=str,
            required=True,
            help="This field cannot be blank"
        )
        parser.add_argument(
            'description',
            type=str,
            required=True,
            help="This field cannot be blank"
        )
        parser.add_argument(
            'posted_by',
            type=int,
            required=True,
            help="This field cannot be blank"
        )
        parser.add_argument(
            'status',
            type=str,
            required=True,
            help="This field cannot be blank"
        )
        parser.add_argument(
            'date_posted',
            type=lambda x: datetime.strptime(x,'%Y-%m-%dT%H:%M:%S'),
            required=True,
            help="This field cannot be blank"
        )
        parser.add_argument(
            'deadline',
            type=lambda x: datetime.strptime(x,'%Y-%m-%dT%H:%M:%S'),
            required=True,
            help="This field cannot be blank"
        )
        data = parser.parse_args()
        job_title = data['title']
        job_description = data['description']
        job_posted_by = data['posted_by']
        job_status = data['status']
        job_posting_date = data['date_posted']
        job_deadline = data['deadline']
        if JobModel.find_by_posted_by_and_title(job_posted_by, job_title):
            return {
                'message': 'Job with Title has been already posted by the recruiter'
            }, 400
        job = JobModel(job_title, job_description, job_posted_by, job_status, job_posting_date, job_deadline)
        job.save_to_db()
        return {
            'message': 'Job successfully created '
        }, 200
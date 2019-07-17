from models.job import JobModel
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_claims, jwt_refresh_token_required, get_raw_jwt
from datetime import datetime

class Job(Resource):
    def get(self, id):
        print("id is " + str(id))
        job = JobModel.find_by_id(id)
        if job != None:
            return job.json(),200
        else:
            return {"error": "Job Not Found"},404

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
        job = JobModel(job_title, job_description, job_posted_by, job_status, job_posting_date, job_deadline)
        job.save_to_db()
        return {
            'message': 'Job successfully created '
        }, 200
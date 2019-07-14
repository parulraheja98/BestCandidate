from models.job import JobModel
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_claims, jwt_refresh_token_required, get_raw_jwt


class Job(Resource):
    def get(self, id):
        print("id is " + str(id))
        job = JobModel.find_by_id(id).json()
        description = job['description']
        posted_by = job['posted_by']
        return {
            'description': description,
            'posted_by': posted_by
        }, 200

class CreateJob(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'description',
            type=str,
            required=True,
            help="This field cannot be blank"
        )
        parser.add_argument(
            'posted_by',
            type=str,
            required=True,
            help="This field cannot be blank"
        )
        data = parser.parse_args()
        job_description = data['description']
        job_posted_by = data['posted_by']

        job = JobModel(job_description, job_posted_by)
        job.save_to_db()
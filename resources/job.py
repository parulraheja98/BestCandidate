from models.job import JobModel


class Job(Resource):
    def get(self):
        job = JobModel.find_by_id(id)


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
        data = Job.parser.parse_args()
        job_description = data.json()['description']
        job_posted_by = data.json()['posted_by']

        job = JobModel(job_description, job_posted_by)
        job.save_to_db()
from models.position import PositionModel

class Position(Resource):
    def get(self):
        position = PositionModel.find_by_id(id)
       

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'name',
            type=str,
            required=True,
            help="This field cannot be blank"
        )
        parser.add_argument(
            'job_id',
            type=int,
            required=True,
            help="This field cannot be blank"
        )
        data = Position.parser.parse_args()
        position_name = data.json()['name']
        job_id = data.json()['job_id']

        position = PositionModel(position_name, job_id)
        position.save_to_db()




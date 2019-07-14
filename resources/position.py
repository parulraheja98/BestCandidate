from models.position import PositionModel
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_claims, jwt_refresh_token_required, get_raw_jwt


class Position(Resource):
    def get(self, id):
        position = PositionModel.find_by_id(id).json()
        print(position)

class PositionByCandidate(Resource):
    def get(self, id):
        position = PositionModel.find_by_candidate(id)
        pos_list_id = []
        for pos in position:
            print(pos.json())

        return position

class CreatePosition(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'name',
            type=str,
            required=True,
            help="This field cannot be blank"
        )
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
        position_name = data['name']
        position_job = data['job']
        position_candidate = data['user']

        job = PositionModel(position_name, position_job, position_candidate)
        job.save_to_db()
       





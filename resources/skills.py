from flask_restful import Resource, reqparse
from tika import parser

class SkillFinder(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'skill',
        type=str,
        required=True,
        help="This field cannot be blank"
    )

    def post(self):
        print("reaching this stage")
        data = SkillFinder.parser.parse_args()
        skill = data['skill']
        data_from_file = parser.from_file('example.pdf')
        list_of_words = data_from_file['content'].split()
        count_for_skillset = 0
        for word in list_of_words:
            if word == skill:
                count_for_skillset = count_for_skillset + 1

        print(count_for_skillset)

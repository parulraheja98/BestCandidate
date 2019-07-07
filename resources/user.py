import hashlib
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )



    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400


        enc_password = hashlib.md5(data['password'].encode())
        user = UserModel(data['username'], enc_password.hexdigest())
        user.save_to_db()

        return {"message": "User created successfully."}, 201


class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="This field cannot be blank"

    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    
    def post(self):
        data = UserLogin.parser.parse_args()
        user_exist = UserModel.find_by_username(data['username'])
        if user_exist:
            password = user_exist.json()['password']
            
            enc_password = hashlib.md5(data['password'].encode())
            if password == enc_password.hexdigest():
                return "Success", 200
            else:
                return "Unsuccesfull",403
        else:
            return "User not found",404

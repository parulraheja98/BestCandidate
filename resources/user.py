import hashlib
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_claims, jwt_refresh_token_required, get_raw_jwt
from models.user import UserModel
from models.application import ApplicationModel
from models.job import JobModel
from blacklist import BLACKLIST


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
    parser.add_argument('role',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )



    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        print(data)
        enc_password = hashlib.md5(data['password'].encode())
        user = UserModel(data['username'], enc_password.hexdigest(),  data['role'])
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

    @jwt_required
    def get(self):
        claims = get_jwt_claims()
        print('checking claim 1')
        print(claims)
        print('checking claim 2')
        return {
            'message': 'success'
        }

    
    def post(self):
        data = UserLogin.parser.parse_args()
        user_exist = UserModel.find_by_username(data['username'])
        print(user_exist.json()['id'])
        user_id = user_exist.json()['id']
        if user_exist:
            password = user_exist.json()['password']  
            print(password)
            enc_password = hashlib.md5(data['password'].encode())
            if password == enc_password.hexdigest():
                access_token = create_access_token(identity=user_id, fresh=True)
                refresh_token = create_refresh_token(user_id)
                return {
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }, 200

    
            else:
                return "Unsuccesfull",403
        else:
            return "User not found",404

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {'access_token': new_token}, 200

class UserLogout(Resource):
    @jwt_required
    def get(self):
        jti = get_raw_jwt()['jti']
        BLACKLIST.add(jti)
        return {
            'message': 'Successfully logged out'
        }, 200


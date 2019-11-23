# import this, so this file has the ability to interact with sqlite3
import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    # to exchange data to webserver
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This Field Cannot Be Blank")

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="jangan dikosongin")

    def post(self):
        # we define what is data in here, which is username and password
        # get the data from user payload
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'username sudah terpakai'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'user created successfully !'}, 201

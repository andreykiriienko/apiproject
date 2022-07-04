from builder.user_builder import UserBuilder
from db_request.user import DataUsers
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/user/create', methods=['POST'])
def create():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        by_username = json.get('username')
        return DataUsers().create_user(data=json).get_user_by_username(username=by_username)
    else:
        return 'Content-Type not supported!'


@app.route('/user/<int:user_id>', methods=['GET'])
def users_get(user_id):
    return UserBuilder().get_user(user_id=user_id).to_json()


@app.route('/user/delete/<int:user_id>', methods=['DELETE'])
def users_delete(user_id):
    request_user_delete = DataUsers().user_delete(user_id=user_id)
    if 'error' in request_user_delete:
        return Response(status=403)
    else:
        return Response(status=204)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(host='0.0.0.0', port=8080, debug=True)

# TODO
## Create User
## /user
##  {"username": "boy", "name": "Vlad"}
##
## Get User
## /user/<id>

from builder.user_builder import UserBuilder
from db_request.user import DataUsers
from db_request.type import DataTypes
from db_request.links import DataLinks
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


@app.route('/type/delete/<int:type_id>', methods=['DELETE'])
def types_delete(type_id):
    request_type_delete = DataTypes().type_delete(type_id=type_id)
    if 'error' in request_type_delete:
        return Response(status=403)
    else:
        return Response(status=204)


@app.route('/link/delete/<int:type_id>', methods=['DELETE'])
def links_delete(link_id):
    request_link_delete = DataLinks().link_delete(link_id=link_id)
    if 'error' in request_link_delete:
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

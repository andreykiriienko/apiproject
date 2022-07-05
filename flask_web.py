from builder.user_builder import UserBuilder
from db_request.user import DataUsers
from db_request.type import DataTypes
from db_request.links import DataLinks
from flask import Flask, request, Response

app = Flask(__name__)

# ===================================================== USER =====================================================
@app.route('/user/create', methods=['POST'])
def create():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        user_by_username = json.get('username')
        create_user = DataUsers().create_user(data=json),
        if 'error' in create_user:
            return Response(status=403)
        return DataUsers().get_user_by_username(username=user_by_username), 201
    else:
        return 'Content-Type not supported!'


@app.route('/user/<int:user_id>', methods=['GET'])
def users_get(user_id):
    return UserBuilder().get_user(id=user_id).to_json()


# ===================================================== TYPE =====================================================
@app.route('/type/create', methods=['POST'])
def type_create():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        create_type = DataTypes().create_type(data=json)
        if 'error' in create_type:
            return Response(status=403)
        else:
            return DataTypes().get_type_by_type_name(data=json), 201
    else:
        return 'Content-Type not supported!'


@app.route('/type/delete/<int:type_id>', methods=['DELETE'])
def types_delete(type_id):
    request_type_delete = DataTypes().type_delete(type_id=type_id)
    if 'error' in request_type_delete:
        return Response(status=403)
    else:
        return Response(status=204)


# ===================================================== LINK =====================================================
@app.route('/link/delete/<int:type_id>', methods=['DELETE'])
def links_delete(link_id):
    request_link_delete = DataLinks().link_delete(link_id=link_id)
    if 'error' in request_link_delete:
        return Response(status=403)
    else:
        return Response(status=204)


@app.route('/link/create/<int:user_id>', methods=['POST'])
def create_link(user_id):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        link_created = DataLinks().create_link(data=json, user_id=user_id)
        if 'error' in link_created:
            return Response(status=403)
        else:
            return DataUsers().get_user_by_id(user_id=user_id), 201
    else:
        return 'Content-Type not supported!'


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

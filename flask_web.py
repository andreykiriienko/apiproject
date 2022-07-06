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


@app.route('/user/delete/<int:user_id>', methods=['DELETE'])
def users_delete(user_id):
    request_user_delete = DataUsers().user_delete(user_id=user_id)
    if 'error' in request_user_delete:
        return Response(status=403)
    else:
        return Response(status=204)


@app.route('/get/all/users', methods=['GET'])
def get_all_user():
    return DataUsers().get_all_users()


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


@app.route('/type/update', methods=['PUT'])
def type_update():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        type_id = json.get('id')
        type = json.get('type')
        return DataTypes().update_type(type_id=type_id, type=type)
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


@app.route('/link/update', methods=['PUT'])
def link_update():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        link_id = json.get('id')
        link = json.get('link')
        return DataLinks().link_update(link_id=link_id, link=link)
    else:
        return 'Content-Type not supported!'


@app.route('/link/delete/<int:link_id>', methods=['DELETE'])
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

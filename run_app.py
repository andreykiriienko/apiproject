from flasgger import Swagger
from builder.user_builder import UserBuilder
from db_request.links import DataLinks
from db_request.user import DataUsers
from db_request.type import DataTypes
from misc import error_processing
from flask import request
from flask import Flask

app = Flask(__name__)
swagger = Swagger(app)


# ===================================================== USER =====================================================
# @app.route('/user/create', methods=['POST'])
def create():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        user_by_username = json.get('username')
        create_user = DataUsers().create_user(data=json)
        get_user = UserBuilder().get_user_by_username(username=user_by_username).to_json()
        return error_processing(create_user, 201, 403, get_user)
    else:
        return 'Content-Type not supported!'


# @app.route('/user/<int:user_id>', methods=['GET'])
def users_get(user_id):
    user_data = UserBuilder().get_user(id=user_id).to_json()
    return error_processing(user_data, 200, 404)


# @app.route('/user/delete/<int:user_id>', methods=['DELETE'])
def users_delete(user_id):
    request_user_delete = DataUsers().user_delete(user_id=user_id)
    return error_processing(request_user_delete, 204, 403)


# @app.route('/user/get', methods=['GET'])
def get_all():
    all_users = DataUsers().get_all_users()
    return error_processing(all_users, 200, 404)


# ===================================================== TYPE =====================================================
# @app.route('/type/create', methods=['POST'])
def type_create():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        create_type = DataTypes().create_type(data=json)
        get_type = DataTypes().get_type_by_type_name(data=json)
        return error_processing(create_type, 201, 403, get_type)
    else:
        return 'Content-Type not supported!'


# @app.route('/type/update', methods=['PUT'])
def type_update():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        update_type = DataTypes().update_type(data=json)
        return error_processing(update_type, 201, 403)
    else:
        return 'Content-Type not supported!'


# @app.route('/type/delete/<int:type_id>', methods=['DELETE'])
def type_delete(type_id):
    request_type_delete = DataTypes().type_delete(type_id=type_id)
    return error_processing(request_type_delete, 204, 403)


# @app.route('/type/get/<int:type_id>', methods=['GET'])
def type_get(type_id):
    get_type = DataTypes().get_type_by_id(type_id=type_id)
    return error_processing(get_type, 200, 404)


# @app.route('/get/all/types', methods=['GET'])
def get_all_types():
    all_types = DataTypes().get_all()
    return error_processing(all_types, 200, 404)


# ===================================================== LINK =====================================================
# @app.route('/link/create', methods=['POST'])
def create_link():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        link = DataLinks().create_link(data=json)
        get_link = UserBuilder().get_user(id=json.get('user_id')).to_json()
        return error_processing(link, 201, 403, get_link)
    else:
        return 'Content-Type not supported!'


# @app.route('/link/get/<int:link_id>', methods=['GET'])
def link_get(link_id):
    get_data_link = DataLinks().get_links_by_id(link_id=link_id)
    return error_processing(get_data_link, 200, 404)


# @app.route('/link/update', methods=['PUT'])
def link_update():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        link = DataLinks().link_update(data=json)
        return error_processing(link, 201, 403)
    else:
        return 'Content-Type not supported!'


# @app.route('/link/delete/<int:link_id>', methods=['DELETE'])
def links_delete(link_id):
    request_link_delete = DataLinks().link_delete(link_id=link_id)
    return error_processing(request_link_delete, 204, 403)


import swagger_doc.types.routes.type_routes

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(debug=True)

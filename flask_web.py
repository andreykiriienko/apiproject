from builder.user_builder import UserBuilder
from db_request.user import DataUsers
from flask import Flask, request

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


@app.route('/user/<int:id>', methods=['GET'])
def users_get(id):
    return UserBuilder().get_user(user_id=id).to_json()


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/user/delete/<int:id>', methods=['DELETE'])
def users_delete(id):
    return DataUsers().user_delete(id)

# TODO
# Create User
# /user
#  {"username": "boy", "name": "Vlad"}
#
# Get User
# /user/<id>

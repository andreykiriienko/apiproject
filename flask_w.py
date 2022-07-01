from flask import Flask, request
from user import DataUsers

app = Flask(__name__)


@app.route('/user/create', methods=['POST'])
def create():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        by_username = json.get('username')
        return DataUsers().create_user(data=json).get_users_by_username(by_username)
    else:
        return 'Content-Type not supported!'


@app.route('/user/<int:id>', methods=['GET'])
def users_get(id):
    return DataUsers().get_user_by_id(id)


if __name__ == '__main__':
    app.run(debug=True)

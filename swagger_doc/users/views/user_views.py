from flasgger import SwaggerView, Schema, fields
from run_app import users_get, get_all, create, users_delete


class User(Schema):
    id = fields.Int()
    username = fields.Str()
    name = fields.Str()
    last_name = fields.Str()
    email = fields.Str()
    password = fields.Str()
    role = fields.Str()
    date_creation = fields.Int()


class UserPost(Schema):
    username = fields.Str()
    name = fields.Str()
    last_name = fields.Str()
    email = fields.Str()
    password = fields.Str()


class UserViewCreate(SwaggerView):
    tags = ['Users']
    parameters = [
        {
            "name": "body",
            "in": "body",
            "type": "string",
            "required": True,
            "schema": UserPost,
        }
    ]
    responses = {
        201: {
            "description": "Successfully created",
            "schema": User
        },
        403: {
            "description": "Access is denied"
        }
    }

    @staticmethod
    def post():
        user_create = create()
        return user_create


class UserViewGetAll(SwaggerView):
    tags = ['Users']
    responses = {
        200: {
            "description": "A list of types",
            "schema": User
        },
        404: {
            "description": "Types not found"
        }
    }

    @staticmethod
    def get():
        get_all_users = get_all()
        return get_all_users


class UserViewGetById(SwaggerView):
    tags = ['Users']
    parameters = [
        {
            "name": "user_id",
            "in": "path",
            "type": "string",
            "required": True,
            "default": ""
        }
    ]
    responses = {
        200: {
            "description": "A list of types",
            "schema": User
        },
        404: {
            "description": "Types not found"
        }
    }

    @staticmethod
    def get(user_id):
        get_user_by_id = users_get(user_id=user_id)
        return get_user_by_id


class UserViewDelete(SwaggerView):
    tags = ['Users']
    parameters = [
        {
            "name": "user_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "default": ""
        }
    ]
    responses = {
        204: {
            "description": "Successfully deleted",
        },
        404: {
            "description": "Not Found"
        }
    }

    @staticmethod
    def delete(user_id):
        delete_user = users_delete(user_id=user_id)
        return delete_user

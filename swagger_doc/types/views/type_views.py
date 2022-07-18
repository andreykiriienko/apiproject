from flasgger import SwaggerView, Schema, fields
from run_app import get_all_types, type_get, type_create, type_delete, type_update


class Type(Schema):
    id = fields.Int()
    type = fields.Str()


class TypeViewCreate(SwaggerView):
    responses = {
        201: {
            "description": "Successfully created",
            "schema": Type
        },
        403: {
            "description": "Access is denied"
        }
    }

    @staticmethod
    def post():
        create = type_create()
        return create


class TypeViewGetAll(SwaggerView):
    responses = {
        200: {
            "description": "A list of types",
            "schema": Type
        },
        404: {
            "description": "Types not found"
        }
    }

    @staticmethod
    def get():
        types = get_all_types()
        return types


class TypeViewGetById(SwaggerView):
    parameters = [
        {
            "name": "Types",
            "in": "query",
            "type": "integer",
            "string": "str",
            "required": True,
            "default": ""
        }
    ]
    responses = {
        200: {
            "description": "A list of types",
            "schema": Type
        },
        404: {
            "description": "Types not found"
        }
    }

    @staticmethod
    def get(type_id):
        get_type = type_get(type_id=type_id)
        return get_type


class TypeViewDelete(SwaggerView):
    parameters = [
        {
            "name": "Types",
            "in": "query",
            "type": "integer",
            "required": True,
            "default": ""
        }
    ]
    responses = {
        204: {
            "description": "Successfully created",
            "schema": Type
        },
        403: {
            "description": "Access is denied"
        }
    }

    @staticmethod
    def delete(type_id):
        delete = type_delete(type_id=type_id)
        return delete


class TypeViewUpdate(SwaggerView):
    parameters = [
        {
            "name": "Types",
            "in": "query",
            "type": "integer",
            "string": "str",
            "required": True,
            "default": ""
        }
    ]
    responses = {
        201: {
            "description": "Successfully",
            "schema": Type
        },
        403: {
            "description": "Access is denied"
        }
    }

    @staticmethod
    def put():
        update = type_update()
        return update










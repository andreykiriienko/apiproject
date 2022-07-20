from flasgger import SwaggerView, Schema, fields
from run_app import create_link, link_get, link_update, links_delete


class Link(Schema):
    id = fields.Int()
    user_id = fields.Int()
    link_type_id = fields.Int()
    link = fields.Str()


class LinkPost(Schema):
    user_id = fields.Int()
    link_type_id = fields.Int()
    link = fields.Str()


class LinkViewCreate(SwaggerView):
    tags = ['Links']
    parameters = [
        {
            "name": "body",
            "in": "body",
            "type": "string",
            "required": True,
            "schema": LinkPost,
        }
    ]
    responses = {
        201: {
            "description": "Successfully created",
            "schema": Link
        },
        403: {
            "description": "Access is denied"
        }
    }

    @staticmethod
    def post():
        link_create = create_link()
        return link_create


class LinkViewGet(SwaggerView):
    tags = ['Links']
    parameters = [
        {
            "name": "link_id",
            "in": "path",
            "type": "string",
            "required": True,
            "default": ""
        }
    ]
    responses = {
        200: {
            "description": "A list of types",
            "schema": Link
        },
        404: {
            "description": "Types not found"
        }
    }

    @staticmethod
    def get(link_id):
        get_link = link_get(link_id=link_id)
        return get_link


class LinkViewUpdate(SwaggerView):
    tags = ['Links']
    parameters = [
        {
            "name": "body",
            "in": "body",
            "type": "string",
            "required": True,
            "schema": Link
        }
    ]
    responses = {
        201: {
            "description": "Successfully",
            "schema": Link
        },
        403: {
            "description": "Access is denied"
        }
    }

    @staticmethod
    def put():
        update_link = link_update()
        return update_link


class LinkViewDelete(SwaggerView):
    tags = ['Links']
    parameters = [
        {
            "name": "link_id",
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
    def delete(link_id):
        delete_link = links_delete(link_id=link_id)
        return delete_link

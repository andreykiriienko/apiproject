from swagger_doc.types.views.type_views import TypeViewCreate, TypeViewGetAll, TypeViewGetById, TypeViewDelete, \
    TypeViewUpdate
from __main__ import app

app.add_url_rule(
    '/type/get',
    view_func=TypeViewGetAll.as_view('type'),
    methods=['GET'],
    provide_automatic_options=False
)

app.add_url_rule(
    '/type/get/<type_id>',
    view_func=TypeViewGetById.as_view('types'),
    methods=['GET'],
    provide_automatic_options=False
)

app.add_url_rule(
    '/type/create',
    view_func=TypeViewCreate.as_view('type_create'),
    methods=['POST'],
    provide_automatic_options=False
)

app.add_url_rule(
    '/type/delete/<type_id>',
    view_func=TypeViewDelete.as_view('type_delete'),
    methods=['DELETE'],
    provide_automatic_options=False
)

app.add_url_rule(
    '/type/update',
    view_func=TypeViewUpdate.as_view('type_update'),
    methods=['PUT'],
    provide_automatic_options=False
)

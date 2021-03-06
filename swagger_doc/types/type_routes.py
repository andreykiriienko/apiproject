from swagger_doc.types.type_views import TypeViewCreate, TypeViewGetAll, TypeViewGetById, TypeViewDelete, \
    TypeViewUpdate

from __main__ import app

app.add_url_rule(
    '/type/get',
    view_func=TypeViewGetAll.as_view('types'),
    methods=['GET']
)

app.add_url_rule(
    '/type/get/<type_id>',
    view_func=TypeViewGetById.as_view('type'),
    methods=['GET']
)

app.add_url_rule(
    '/type/create',
    view_func=TypeViewCreate.as_view('type_create'),
    methods=['POST']
)

app.add_url_rule(
    '/type/delete/<type_id>',
    view_func=TypeViewDelete.as_view('type_delete'),
    methods=['DELETE']
)

app.add_url_rule(
    '/type/update',
    view_func=TypeViewUpdate.as_view('type_update'),
    methods=['PUT']
)

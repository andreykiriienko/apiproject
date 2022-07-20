from swagger_doc.users.views.user_views import UserViewGetAll, UserViewGetById, UserViewCreate, UserViewDelete

from __main__ import app

app.add_url_rule(
    '/user/create',
    view_func=UserViewCreate.as_view('users_create'),
    methods=['POST']
)

app.add_url_rule(
    '/user/get',
    view_func=UserViewGetAll.as_view('users'),
    methods=['GET']
)

app.add_url_rule(
    '/user/<int:user_id>',
    view_func=UserViewGetById.as_view('user'),
    methods=['GET']
)

app.add_url_rule(
    '/user/delete/<int:user_id>',
    view_func=UserViewDelete.as_view('users_delete'),
    methods=['DELETE']
)
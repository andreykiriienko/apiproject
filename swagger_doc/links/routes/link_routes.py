from swagger_doc.links.views.link_views import LinkViewCreate, LinkViewGet, LinkViewUpdate, LinkViewDelete

from __main__ import app

app.add_url_rule(
    '/link/create',
    view_func=LinkViewCreate.as_view('link_create'),
    methods=['POST']
)

app.add_url_rule(
    '/link/get/<int:link_id>',
    view_func=LinkViewGet.as_view('link'),
    methods=['GET']
)

app.add_url_rule(
    '/link/update',
    view_func=LinkViewUpdate.as_view('link_update'),
    methods=['PUT']
)

app.add_url_rule(
    '/link/delete/<int:link_id>',
    view_func=LinkViewDelete.as_view('link_delete'),
    methods=['DELETE']
)

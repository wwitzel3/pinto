from pyramid.view import view_config

@view_config(route_name='admin_index',
             renderer='pinto:admin/templates/index.mako')
def index(request):
    return {}


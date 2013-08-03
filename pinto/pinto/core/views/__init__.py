from pyramid.view import view_config

@view_config(route_name='index', context='pinto.core.resources.Root',
             renderer='pinto:core/templates/index.mako')
def index(request):
    return {}


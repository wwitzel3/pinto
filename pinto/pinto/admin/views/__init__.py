from pyramid.security import (
    remember,
    forget,
)
from pyramid.view import (
    view_config,
    forbidden_view_config,
)
from pyramid.httpexceptions import HTTPFound

@view_config(route_name='admin_index', permission='admin',
             renderer='pinto:admin/templates/index.mako')
def index(request):
    return {}

@view_config(route_name='admin_login', permission='view',
             renderer='pinto:admin/templates/login.mako')
@forbidden_view_config(renderer='pinto:admin/templates/login.mako')
def login(request):
    login_url = request.route_url('admin_login')
    referrer = request.url
    if referrer == login_url:
        referrer = '/'
    came_from = request.params.get('came_from', referrer)

    if 'form.submitted' in request.params:
        login_url = request.route_url('admin_login')
        referrer = request.url
        if referrer == login_url:
            referrer = '/'
        came_from = request.params.get('came_from', referrer)
        headers = remember(request, 'admin')
        return HTTPFound(location = came_from,
                         headers = headers)
    return {'came_from':came_from}

@view_config(route_name='admin_logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = request.route_url('admin_index'),
                     headers = headers)

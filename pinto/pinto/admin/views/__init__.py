from pyramid.security import (
    authenticated_userid,
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
    owner = authenticated_userid(request)
    return {}

@view_config(route_name='admin_login', permission='view',
             renderer='pinto:admin/templates/login.mako')
@forbidden_view_config(renderer='pinto:admin/templates/login.mako')
def login(request):
    if 'form.submitted' in request.params:
        headers = remember(request, 'admin')
        return HTTPFound(location = request.route_url('admin_index'),
                         headers = headers)
    return {}

@view_config(route_name='admin_logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = request.route_url('admin_index'),
                     headers = headers)

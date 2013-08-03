from pyramid.view import view_config

@view_config(route_name='post', context='pinto.post.resources.Root',
             renderer='pinto:post/templates/post.mako')
def post(request):
    return {}

@view_config(route_name='post_new', context='pinto.post.resources.Root',
             permission='admin', renderer='pinto:post/templates/new.mako')
def post_new(request):
    return {}

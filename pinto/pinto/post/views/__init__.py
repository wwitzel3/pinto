from pyramid.view import view_config

@view_config(route_name='post', context='pinto.post.resources.Root',
             renderer='pinto:post/templates/post.mako')
def post(request):
    return {}


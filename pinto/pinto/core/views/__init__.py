from pyramid.view import view_config

from pinto.post.model import get_recent_posts

@view_config(route_name='index', context='pinto.core.resources.Root',
             renderer='pinto:core/templates/index.mako')
def index(request):
    posts = get_recent_posts(request)
    return {'posts':posts}


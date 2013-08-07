from pyramid.view import view_config

from pinto.post.model import (
    get_recent_posts,
    get_tags,
)

@view_config(route_name='index', renderer='pinto:core/templates/index.mako')
def index(request):
    posts = get_recent_posts(request)
    tags = get_tags(request)

    return {
        'posts':posts,
        'tags':tags,
    }

@view_config(route_name='about', renderer='pinto:core/templates/about.mako')
def about(request):
    return {}


from pyramid.view import view_config

from pinto.post.model import get_recent_posts_in_tags

@view_config(route_name='category',
             renderer='pinto:category/templates/index.mako')
def category(request):
    posts = get_recent_posts_in_tags(request, [request.matchdict['tag'],])
    return {
        'posts':posts,
    }


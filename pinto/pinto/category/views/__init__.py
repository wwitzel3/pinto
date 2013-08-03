from pyramid.view import view_config

@view_config(route_name='category', context='pinto.category.resources.Root',
             renderer='pinto:category/templates/category.mako')
def category(request):
    return {}


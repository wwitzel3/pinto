from collections import namedtuple

import deform

from slugify import slugify

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from pinto.post.schema import Post
from pinto.post.model import get_post

@view_config(route_name='post', renderer='pinto:post/templates/post.mako')
def post(request):
    return get_post(request)

@view_config(route_name='post_new', permission='admin',
             renderer='pinto:post/templates/new.mako')
def post_new(request):
    url = request.POST.get('url','')
    schema = Post().bind(request=request, url=url,
                         markdown=request.POST.get('markdown',''))
    form = deform.Form(schema)
    if 'form.submitted' in request.params:
        try:
            appstruct = form.validate(request.POST.items())
            request.db.post.insert(appstruct)

            return HTTPFound(location = request.route_url('post', key=appstruct.get('url')))
        except deform.ValidationFailure as e:
            pass

    form_dict = {f.name:f for f in form}
    Form = namedtuple('Form', ','.join(form_dict.keys()))
    form = Form._make(form_dict.values())
    return {
        'form':form,
    }

@view_config(route_name='post_slug', permission='admin', renderer='json')
def post_slug(request):
    return {'slug':slugify(request.GET.get('title'))}

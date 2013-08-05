from collections import namedtuple

import deform

from slugify import slugify

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from pinto.post.schema import Post

@view_config(route_name='post', context='pinto.post.model.Post',
             renderer='pinto:post/templates/post.mako')
def post(context, request):
    post = context.get()
    return post

@view_config(route_name='post_new', context='pinto.post.resources.Root',
             permission='admin', renderer='pinto:post/templates/new.mako')
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

@view_config(route_name='post_slug', context='pinto.post.resources.Root',
             permission='admin', renderer='json')
def post_slug(request):
    return {'slug':slugify(request.GET.get('title'))}

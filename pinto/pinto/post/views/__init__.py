import deform

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
    schema = Post().bind(request=request,
                         url=request.POST.get('url'),
                         title=request.POST.get('title',''))
    form = deform.Form(schema)

    if 'form.submitted' in request.params:
        try:
            appstruct = form.validate(request.POST.items())
            request.db.post.insert(appstruct)

            return HTTPFound(location = request.route_url('post', key=appstruct.get('url')))
        except deform.ValidationFailure as e:
            pass

    return {
        'form':form,
    }

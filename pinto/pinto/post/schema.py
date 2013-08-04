from slugify import slugify
import colander as c

@c.deferred
def deferred_url_validator(node, kw):
    """Check to make sure that another post is not already
    using our url slug
    """
    request = kw.get('request')
    post = request.db.post.find_one({'url':kw.get('url')})
    if post:
        def invalid_url(node, value):
            raise c.Invalid(node, u"A post with that url already exists.")
        return invalid_url

class Tags(c.SchemaType):
    """Uses a standard text input
    Expects to see a comma seperated list of tags
    """
    def serialize(self, node, appstruct):
        if appstruct in (c.null, None):
            return ''
        appstruct = ','.join(appstruct)
        return appstruct

    def deserialize(self, node, cstruct):
        if not cstruct:
            return c.null
        cstruct = [slugify(t.strip()) for t in cstruct.split(',')]
        return cstruct


class Post(c.MappingSchema):
    url = c.SchemaNode(c.String(), validator=deferred_url_validator)
    title = c.SchemaNode(c.String())
    body = c.SchemaNode(c.String())
    tags = c.SchemaNode(Tags())

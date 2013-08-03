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

class Post(c.MappingSchema):
    url = c.SchemaNode(c.String(), validator=deferred_url_validator)
    body = c.SchemaNode(c.String())



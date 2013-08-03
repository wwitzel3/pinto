import colander as c

class Post(c.MappingSchema):
    url = c.SchemaNode(c.String())
    body = c.SchemaNode(c.String())



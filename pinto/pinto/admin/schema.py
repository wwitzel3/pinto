import colander as c

class Settings(c.MappingSchema):
    title = c.SchemaNode(c.String(), if_missing='Blog')
    subtitle = c.SchemaNode(c.String(), if_missing='This is my blog.')
    email = c.SchemaNode(c.String(), if_missing='user@example.com')


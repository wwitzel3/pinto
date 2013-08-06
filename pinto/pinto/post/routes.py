from pinto.security import RootACL

class Root(RootACL):
    pass

def includeme(config):
    config.add_route('post_new', '/new', factory=Root)
    config.add_route('post_slug', '/api/slugify', factory=Root)
    config.add_route('post', '/{url}', factory=Root)

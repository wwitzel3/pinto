from pinto.security import RootACL

class Root(RootACL):
    pass

def includeme(config):
    config.add_route('admin_index', '/', factory=Root)
    config.add_route('admin_login', '/login', factory=Root)
    config.add_route('admin_logout', '/logout', factory=Root)


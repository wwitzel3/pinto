from pinto.admin.security import Root

def includeme(config):
    config.add_route('admin_index', '/', factory=Root)
    config.add_route('admin_login', '/login', factory=Root)
    config.add_route('admin_logout', '/logout', factory=Root)


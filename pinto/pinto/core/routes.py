from pinto.security import RootACL

class Root(RootACL):
    pass

def includeme(config):
     config.add_route('about', '/about', factory=Root)
     config.add_route('index', '/', factory=Root)


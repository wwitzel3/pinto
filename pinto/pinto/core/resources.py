class Root(object):
    def __init__(self, request):
        pass

def includeme(config):
    config.add_route('index', '/', factory=Root)

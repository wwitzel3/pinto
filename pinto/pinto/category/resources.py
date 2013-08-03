from pinto.category.model import Category

class Root(object):
    __name__ = ''
    __parent__ = None

    def __init__(self, request):
        self.request = request

    def __getitem__(self, key):
        if key:
            return Category(self.request, key)
        raise KeyError

def includeme(config):
    config.add_route('category', '/{key}', factory=Root)


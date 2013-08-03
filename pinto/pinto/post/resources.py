from pinto.post.model import Post

class Root(object):
    __name__ = ''
    __parent__ = None

    def __init__(self, request):
        self.request = request

    def __getitem__(self, key):
        if key:
            return Post(self.request, key)
        raise KeyError

def includeme(config):
    config.add_route('post', '/{key}', factory=Root)


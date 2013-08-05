from pinto.security import RootACL
from pinto.post.model import Post

class Root(RootACL):
    __name__ = ''
    __parent__ = None

    def __getitem__(self, key):
        if key:
            return Post(self.request, key)
        raise KeyError

def includeme(config):
    config.add_route('post_new', '/new', factory=Root)
    config.add_route('post_slug', '/api/slugify', factory=Root)
    config.add_route('post', '/{key}', factory=Root, traverse='{key}')

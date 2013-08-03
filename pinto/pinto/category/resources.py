from pinto.security import RootACL
from pinto.category.model import Category

class Root(RootACL):
    __name__ = ''
    __parent__ = None

    def __getitem__(self, key):
        if key:
            return Category(self.request, key)
        raise KeyError

def includeme(config):
    config.add_route('category', '/{key}', factory=Root, traverse='{key}')


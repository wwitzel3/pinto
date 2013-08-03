class Post(object):
    def __init__(self, request, key):
        self.db = request.db
        self.__name__ = key

    def get(self):
        return self.db.post.find_one({'url':self.__name__})


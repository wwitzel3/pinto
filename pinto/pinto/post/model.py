class Post(object):
    def __init__(self, request, key):
        self.db = request.db
        self.__name__ = key

    def get(self):
        return self.db.post.find_one({'url':self.__name__})


def page_results(results, num_of_posts, page):
    row = num_of_posts * (page-1)
    return results[row:row+num_of_posts]

def get_recent_posts(request, num_of_posts=10, page=1):
    posts = request.db.post.find({'active':True}).sort('_id',-1)
    return page_results(posts, num_of_posts, page)

def get_recent_posts_in_category(request, category, num_of_posts=10, page=1):
    posts = request.db.post.find({'active':True,
                                  'category':category}).sort('_id',-1)
    return page_results(posts, num_of_posts, page)


def get_post(request):
    return request.db.post.find_one({'url':request.matchdict['url']})

def page_results(results, num_of_posts, page):
    row = num_of_posts * (page-1)
    return results[row:row+num_of_posts]

def get_recent_posts(request, num_of_posts=10, page=1):
    posts = request.db.post.find({'active':True}).sort('_id',-1)
    return page_results(posts, num_of_posts, page)

def get_recent_posts_in_tags(request, tags, num_of_posts=10, page=1):
    posts = request.db.post.find({'active':True,
                                  'tags': {'$in': tags}}).sort('_id',-1)
    return page_results(posts, num_of_posts, page)

def get_tags(request):
    result = request.db.command('distinct', 'post', key='tags')
    return result.get('values')


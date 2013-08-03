from pyramid.security import (
    Allow,
    Everyone,
    ALL_PERMISSIONS,
)

class Root(object):
    __acl__ = [
        (Allow, Everyone, 'view'),
        (Allow, 'admin', ALL_PERMISSIONS)
    ]

    def __init__(self, request):
        self.request = request

def groupfinder(userid, request):
    user = request.db.user.find_one({'user':userid})
    if user:
        return user.get('groups')


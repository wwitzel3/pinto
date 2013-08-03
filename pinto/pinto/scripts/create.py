import os
import sys
from urlparse import urlparse

import pymongo

from pyramid.paster import (
    bootstrap,
    setup_logging
)

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)

    config_uri = argv[1]
    setup_logging(config_uri)
    env = bootstrap(config_uri)
    settings = env['registry'].settings

    mongo_url = urlparse(settings['mongo_uri'])
    client = pymongo.MongoClient(mongo_url.hostname, mongo_url.port)
    db = client[mongo_url.path[1:]]
    db.user.insert({'user':'admin', 'password':'password', 'groups':['admin']})

if __name__ == '__main__':
    main()

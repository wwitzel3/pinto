from urlparse import urlparse

import pymongo

from pinto.core.interfaces import IMongoDBMaker

def get_mongo_db(request):
    db = request.registry.getUtility(IMongoDBMaker)

    def cleanup(request):
        db.connection.close()

    request.add_finished_callback(cleanup)
    return db

def includeme(config):
    mongo_url = urlparse(config.registry.settings['mongo_uri'])
    client = pymongo.MongoClient(mongo_url.hostname, mongo_url.port)
    database = client[mongo_url.path[1:]]
    config.registry.registerUtility(database, IMongoDBMaker)

    config.add_request_method(get_mongo_db, 'db', reify=True)
    config.include('pinto.core.resources')


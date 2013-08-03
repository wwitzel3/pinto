from urlparse import urlparse

import pymongo

from pinto.core.interfaces import IMongoClientMaker

def get_mongo_client(request):
    client = request.registry.getUtility(IMongoClientMaker)

    def cleanup(request):
        client.close()

    request.add_finish_callback(cleanup)
    return client

def includeme(config):
    mongo_url = urlparse(config.registry.settings['mongo_uri'])
    client = pymongo.MongoClient(mongo_url.hostname, mongo_url.port)
    config.registry.registerUtility(client, IMongoClientMaker)

    config.add_request_method(get_mongo_client, 'db', reify=True)
    config.include('pinto.core.resources')


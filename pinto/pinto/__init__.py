import os

from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig

here = os.path.dirname(__file__)

def setup_includes(config):
    config.include('pinto.core')
    config.include('pinto.post', route_prefix='/post')
    config.include('pinto.category', route_prefix='/category')

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    session_factory = UnencryptedCookieSessionFactoryConfig('supersekret')
    config = Configurator(settings=settings, session_factory=session_factory)
    config.add_static_view('static', 'static', cache_max_age=3600)

    setup_includes(config)

    config.scan()
    return config.make_wsgi_app()

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pinto.admin.security import groupfinder

def includeme(config):
    authn_policy = AuthTktAuthenticationPolicy(
        config.registry.settings['auth.secret'],
        callback=groupfinder,
    )
    authz_policy = ACLAuthorizationPolicy()

    config.include('pinto.admin.routes')
    config.set_authorization_policy(authz_policy)
    config.set_authentication_policy(authn_policy)


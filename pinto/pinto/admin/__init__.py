def get_site_settings(request):
    return request.db.settings.find_one()

def includeme(config):
    config.add_request_method(get_site_settings, 'settings', reify=True)
    config.include('pinto.admin.routes')


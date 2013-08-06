<%inherit file="pinto:core/templates/base.mako"/>
<%namespace name="h" file="pinto:core/templates/lib/helpers.mako"/>

<ul>
    <li><a href="${request.route_url('post_new')}">Add Post</a></li>
    <li><a href="${request.route_url('admin_settings')}">Site Settings</a></li>
    <li><a href="${request.route_url('admin_logout')}">Logout</a></li>
</ul>

<%def name="value(field)">
<%
from colander import null
%>
% if field.cstruct in (null, None):
${''}
% else:
${field.cstruct}
% endif
</%def>

<%def name="render_tags(request, tags)">
${', '.join(['<a href="%s">%s</a>' % (request.route_url('category', tag=t),t) for t in tags]) | n}
</%def>

<%def name="serialize(widget, label)">
<label for="${widget.title.lower()}">${label}</label>
<% error_css = 'error' if widget.error else None %>
${widget.serialize(css_class=error_css) | n}
% if error_css:
<small class="${error_css}">${','.join(widget.error.messages())}</small>
% endif
</%def>

<%inherit file="pinto:core/templates/base.mako"/>

<form action="${request.route_url('post_new')}" method="POST">
<input type="hidden" name="form.submitted" value="1"/>
% for field in form:
<div>${field.title}</div>
<div>${field.serialize() | n}</div>
% if field.error:
<div>
%for error in field.error.messages():
${error},
%endfor
%endif
</hr>
%endfor
<input type="submit"/>
</form>

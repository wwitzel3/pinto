<%inherit file="pinto:core/templates/base.mako"/>
<%namespace name="h" file="pinto:core/templates/lib/helpers.mako"/>

<form action="${request.route_url('post_new')}" method="POST">
<input type="hidden" name="form.submitted" value="1">

<fieldset>
<legend>New blog post</legend>

<label for="title">Title</label>
<% error_css = "error" if form.title.error else None %>
${form.title.serialize(css_class=error_css) | n}
% if error_css:
<small class="error">${','.join(form.title.error.messages())}</small>
% endif

<label for="url">URL (Slug)</label>
<% error_css = "error" if form.url.error else None %>
${form.url.serialize(css_class=error_css) | n}
% if error_css:
<small class="error">${','.join(form.url.error.messages())}</small>
% endif

<label for="tags">Tags</label>
<% error_css = "error" if form.tags.error else None %>
${form.tags.serialize(css_class=error_css) | n}
% if error_css:
<small class="error">${','.join(form.tags.error.messages())}</small>
% endif

<label for="active">Publish</label>
${form.active.serialize() | n}

${form.markdown.serialize() | n}
<div id="editor"></div>

</fieldset>

<input class="large button expanded" type="submit" value="Save Post">
</form>

<script src="${request.static_url('pinto:static/javascripts/ace/ace.js')}" type="text/javascript" charset="utf-8"></script>
<script>
    var editor = ace.edit('editor');
    var textarea = $('textarea[name="markdown"]').hide();
    editor.setTheme('ace/theme/clouds');
    editor.getSession().setMode('ace/mode/markdown');
    editor.getSession().setValue(textarea.val());
    editor.getSession().on('change', function() {
        textarea.val(editor.getSession().getValue());
    });

    var url = $('input[name="url"]');
    $('input[name="title"]').on('blur', function() {
        $.get("${request.route_url('post_slug')}",
              {title: $(this).val()}).done(function(data) { url.val(data.slug); });
    });
</script>


<%inherit file="pinto:core/templates/base.mako"/>
<%namespace name="h" file="pinto:core/templates/lib/helpers.mako"/>

<form action="${request.route_url('post_new')}" method="POST">
<input type="hidden" name="form.submitted" value="1">

<fieldset>
<legend>New blog post</legend>

${h.serialize(form.title, 'Title')}
${h.serialize(form.url, 'URL (Slug)')}
${h.serialize(form.tags, 'Tags')}

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


<%inherit file="pinto:core/templates/base.mako"/>
<%namespace name="h" file="pinto:core/templates/lib/helpers.mako"/>

      <article>

        <h3><a href="${request.route_url('post', url=url)}">${title}</a></h3>
        <h6>Written by <a href="#">Wayne Witzel III</a> on ${date.strftime('%B %d, %Y')}.</h6>

        ${body | n}

        <small><strong>Tags:</strong> ${h.render_tags(request,tags)}</small>
        </article>


<%inherit file="pinto:core/templates/base.mako"/>

      <article>

        <h3><a href="${request.route_url('post', key=url)}">${title}</a></h3>
        <h6>Written by <a href="#">Wayne Witzel III</a> on ${date.strftime('%B %d, %Y')}.</h6>

        ${body | n}

        <small>Tags: ${','.join(['<a href="#">%s</a>'% t for t in tags]) | n}</small>
      </article>


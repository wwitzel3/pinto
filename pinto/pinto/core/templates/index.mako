<%inherit file="pinto:core/templates/base.mako"/>
<%namespace name="h" file="pinto:core/templates/lib/helpers.mako"/>

      % for post in posts:
      <article>

        <h3><a href="${request.route_url('post', url=post.get('url'))}">${post.get('title')}</a></h3>
        <h6>Written by <a href="#">Wayne Witzel III</a> on ${post.get('date').strftime('%B %d, %Y')}.</h6>

        ${post.get('body') | n}

        <small><strong>Tags:</strong> ${h.render_tags(request, post.get('tags'))}</small>
      </article>
      <hr/>
      % endfor

<%def name="sidebar()">
      <div>
        <h5>Categories</h5>
        <ul class="side-nav">
        ${h.render_tags(request,tags)}
        </ul>
      </div>

      <div class="panel">
        <h5>Featured</h5>
        <p>Pork drumstick turkey fugiat. Tri-tip elit turducken pork chop in. Swine short ribs meatball irure bacon nulla pork belly cupidatat meatloaf cow.</p>
        <a href="#">Read More &rarr;</a>
      </div>
</%def>

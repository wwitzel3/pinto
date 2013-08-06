<%inherit file="pinto:core/templates/base.mako"/>

      % for post in posts:
      <article>

        <h3><a href="${request.route_url('post', url=post.get('url'))}">${post.get('title')}</a></h3>
        <h6>Written by <a href="#">Wayne Witzel III</a> on ${post.get('date').strftime('%B %d, %Y')}.</h6>

        ${post.get('body') | n}
      </article>
      <hr/>
      % endfor

<%def name="sidebar()">
      <div class="panel">
        <h5>Featured</h5>
        <p>Pork drumstick turkey fugiat. Tri-tip elit turducken pork chop in. Swine short ribs meatball irure bacon nulla pork belly cupidatat meatloaf cow.</p>
        <a href="#">Read More &rarr;</a>
      </div>
</%def>

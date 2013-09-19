<%inherit file="pinto:core/templates/base.mako"/>
<%namespace name="h" file="pinto:core/templates/lib/helpers.mako"/>

    <article>

        <h3>About</h3>

        ${request.settings.get('about')}

    </article>

    <p>
    I am a developer living in Florida currently working for <a href="http://sf.net">SourceForge</a>
    developing <a href="http://sf.net/p/allura">Allura</a>, the open project hosting platform that powers
    SourceForge.</p>

    <p>I primarily program in Python but try to experiment and play with a new
    language every year. Currently I am learning Go.</p>

    <p>I like the <a href="http://docs.pylonsproject.org/en/latest/docs/pyramid.html">Pyramid</a> and <a href="http://www.sqlalchemy.org/">SQLalchemy</a> and there and try to
    give back to these communities through my blog posts, mailing list help,
    patches, and IRC help.</p>

    <p>If you like my work or have benefited from it in some way, consider
    giving back.

    <ul>
      <li>Follow <a href="https://twitter.com/wwitzel3">@wwitzel3</a> on Twitter</li>
      <li>Tip me 
        <iframe style="border: 0; margin: 0; padding: 0;"
              src="https://www.gittip.com/wwitzel3/widget.html"
              width="48pt" height="20pt">
        </iframe>
      </li>
      <li>Donate to the <a href="http://www.python.org/psf/donations/">Python Software Foundation</a></li>
      </ul>
    </p>
  </span>
</div>

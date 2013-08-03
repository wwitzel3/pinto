pinto
=====

pinto is a Pyramid blogging system. I created it so that I had a Pyramid site to hack on.
pinto requires mongodb and uses Mako templates and the Foundation CSS library.

* gem update --system
* gem install compass
* gem install zurb-Foundation
* python setup.py install
* pinto_create_db development.ini
* compass compile
* pserve development.ini

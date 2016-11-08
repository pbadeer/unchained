import os
import sys
import site

# Add virtual environment packages to site directory
site.addsitedir('~/.virtualenvs/unchained/local/lib/python2.7/site-packages')

# Add project path to the sys.path
sys.path.append('/var/www/html/')

# Import Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "unchained.settings")

# Activate virtual environment
activate_env = os.path.expanduser(
    "/home/ubuntu/.virtualenvs/unchained/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

# Don't move this import!
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
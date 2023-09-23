import imp
import os
import sys

PASSENGER_APP_ENV = 'development'

sys.path.insert(0, os.path.dirname(__file__))

wsgi = imp.load_source('wsgi', 'app.py')
application = wsgi.app
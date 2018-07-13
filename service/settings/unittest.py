from service.settings.defaults import *

# Turn off debugging when running the tests
DEBUG = False
TEMPLATE_DEBUG = False

# Define the in memory database to be used
DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'unit_test_db',
    }
}
import datetime

from service.settings.defaults import *


DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'service_db',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get('DATABASE_NAME', 'service_db'),
#         'USER': os.environ.get('DATABASE_USER', 'micro'),
#         'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'service'),
#         'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
#         'PORT': os.environ.get('DATABASE_PORT', '5432'),
#     }
# }

# Absolute filesystem path to the directory that will hold user-uploaded files.
PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Go down one level for the media-files
MEDIA_ROOT = '/opt/service/media-files'
MEDIA_URL = "http://localhost:8000/service/media/"

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(PROJECT_ROOT, os.pardir, 'static-files')

# Set the default token authentication token timeouts
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=14),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=14)
}

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Tell nose to measure coverage on the applications
NOSE_ARGS = [
    # '--with-coverage',
    # '--cover-package=api', # Restrict coverage to selected packages
    '--cover-erase',  # Remove coverage results from the last run
    '--cover-html',  # Enable HTML report
    '--cover-inclusive',  # Scan all files in the working directories
]
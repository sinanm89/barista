DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'barista',                      # Or path to database file if using sqlite3.
        'USER': 'baristadbu',                      # Not used with sqlite3.
        'PASSWORD': 'vagrant',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

ROOT_MEDIA_URL = 'http://snn.local/'
MEDIA_URL = ROOT_MEDIA_URL + '/'
STATIC_URL = ROOT_MEDIA_URL

KIBRIT_PATH = '/home/vagrant/barista/src/barista/'

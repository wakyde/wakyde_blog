from .base import * # NOQA


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#        'USER':'root',
#        'PASSWORD':'051998',
#        'HOST':'localhost',
#        'PORT':'3306',
    }
}


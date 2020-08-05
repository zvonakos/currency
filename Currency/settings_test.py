from Currency.settings import *  # noqa

SECRET_KEY = 'krne$j#+#c&tzxe_x96est8c*63s$9t6wbt=ewi6gih7&dbj)w'
DEBUG = False
ALLOWED_HOSTS = ['*']

CELERY_ALWAYS_EAGER = CELERY_TASK_ALWAYS_EAGER = True  # run celery tasks as func

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db-test.sqlite3'),  # noqa
    }
}

EMAIL_BACKEND = 'django.core.mail.outbox'

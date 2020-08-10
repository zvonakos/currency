SECRET_KEY = 'krne$j#+#c&tzxe_x96est8c*63s$9t6wbt=ewi6gih7&dbj)w'

DEBUG = True
ALLOWED_HOSTS = ['*']

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'email@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
 DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
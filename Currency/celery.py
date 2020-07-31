import os  # noqa
from celery import Celery  # noqa

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Currency.settings')

app = Celery('currency_exchange')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

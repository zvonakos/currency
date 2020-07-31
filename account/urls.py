from account import views  # noqa
from django.urls import path  # noqa


app_name = 'account'


urlpatterns = [
    path('smoke/', views.smoke, name='smoke'),
]

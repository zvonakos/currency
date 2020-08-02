from account import views  # noqa
from django.contrib.auth.views import LoginView, LogoutView  # noqa
from django.urls import path  # noqa


app_name = 'account'


urlpatterns = [
    path('smoke/', views.smoke, name='smoke'),
    path('contact-us/', views.ContactUs.as_view(), name='contact-us'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.MyProfile.as_view(), name='profile'),
]

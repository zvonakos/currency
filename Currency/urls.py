from django.contrib import admin  # noqa
from django.views.generic import TemplateView  # noqa
from django.conf import settings  # noqa
from django.urls import include, path  # noqa

from Currency import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='index.html',), name='index'),

    path('account/', include('account.urls')),
    path('rate/', include('rate.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


handler404 = views.handler404
handler500 = views.handler500


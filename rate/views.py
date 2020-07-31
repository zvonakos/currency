from django.views.generic import ListView  # noqa
from rate.models import Rate  # noqa


class RateList(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate-list.html'

from account.models import Contact, User  # noqa
from account.tasks import send_email_async  # noqa
from django.http import HttpResponse  # noqa

from django.contrib.auth.mixins import LoginRequiredMixin  # noqa
from django.urls import reverse_lazy  # noqa
from django.views.generic import CreateView, UpdateView  # noqa


def smoke(request):
    return HttpResponse('Hello from account')


class ContactUs(CreateView):
    template_name = 'contact-us.html'
    model = Contact
    fields = 'email_from', 'subject', 'message'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        send_email_async.delay(form.cleaned_data)
        return result


class MyProfile(LoginRequiredMixin, UpdateView):
    template_name = 'user-edit.html'
    model = User
    fields = 'email', 'first_name', 'last_name'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        obj = self.get_queryset().get(id=self.request.user.id)
        return obj

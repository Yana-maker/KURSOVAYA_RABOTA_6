from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from mailing.forms import Text_MailingForm, ClientForm
from mailing.models import Text_Mailing, Client


class MailingCreateView(CreateView):
    model = Text_Mailing
    form_class = Text_MailingForm
    success_url = reverse_lazy('mailing:list')

    extra_context = {
        'title': 'СОЗДАНИЕ РАССЫЛКИ'
    }


class MailingListView(ListView):
    model = Text_Mailing
    form_class = Text_MailingForm
    extra_context = {
        'title': 'рассылки'
    }

class MailingUpdateView(UpdateView):
    model = Text_Mailing
    success_url = reverse_lazy('mailing:list')

    extra_context = {
        'title': 'РЕДАКТИРОВАНИЕ РАССЫЛКИ'
    }

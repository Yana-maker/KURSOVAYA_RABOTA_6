from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from mailing.forms import Text_MailingForm, ClientForm, Log_MailingForm
from mailing.models import Text_Mailing, Client, Log_Mailing


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:list')

    extra_context = {
        'title': 'ДОБАВЛЕИНЕ ПОЛЬЗОВАТЕЛЯ ДЛЯ РАССЫЛОК'
    }


class ClientListView(ListView):
    model = Client
    form_class = ClientForm

    extra_context = {
        'title': 'СПИСОК ПОЛЬЗОВАТЕЛЕЙ ДЛЯ РАССЫЛОК'
    }


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
        'title': 'РАССЫЛКИ'
    }


class MailingUpdateView(UpdateView):
    model = Text_Mailing
    success_url = reverse_lazy('mailing:list')

    extra_context = {
        'title': 'РЕДАКТИРОВАНИЕ РАССЫЛКИ'
    }


class Log_MailingListView(ListView):
    model = Log_Mailing
    form_class = Log_MailingForm

    extra_context = {
        'title': 'ПРОСМОТР ЛОГОВ'
    }

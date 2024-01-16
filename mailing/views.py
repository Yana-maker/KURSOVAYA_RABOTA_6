from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from mailing.forms import Text_MailingForm, ClientForm, Log_MailingForm, MailingForm
from mailing.models import Text_Mailing, Client, Log_Mailing, Mailing


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:list')

    extra_context = {
        'title': 'ДОБАВЛЕНИЕ ПОЛЬЗОВАТЕЛЯ ДЛЯ РАССЫЛОК'
    }


class ClientListView(ListView):
    model = Client
    form_class = ClientForm

    extra_context = {
        'title': 'СПИСОК ПОЛЬЗОВАТЕЛЕЙ ДЛЯ РАССЫЛОК'
    }


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm

    extra_context = {
        'title': 'РЕДАКТИРОВАНИЕ ПОЛЬЗОВАТЕЛЕЙ ДЛЯ РАССЫЛОК'
    }


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:list')

    extra_context = {
        'title': 'СОЗДАНИЕ ПЕРИОДИЧНОСТИ ДЛЯ РАССЫЛКИ'
    }


class MailingListView(ListView):
    model = Mailing
    form_class = MailingForm

    extra_context = {
        'title': 'ПРОСМОТР СПИСКА ПЕРИОДИЧНОСТИ РАССЫЛОК'
    }


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:list')

    extra_context = {
        'title': 'РЕДАКТИРОВАНИЕ ПЕРИОДИЧНОСТИ РАССЫЛКИ'
    }


class Text_MailingCreateView(CreateView):
    model = Text_Mailing
    form_class = Text_MailingForm
    success_url = reverse_lazy('mailing:list')

    extra_context = {
        'title': 'СОЗДАНИЕ ТЕКСТА ДЛЯ РАССЫЛКИ'
    }


class Text_MailingListView(ListView):
    model = Text_Mailing
    form_class = Text_MailingForm

    extra_context = {
        'title': 'ПРОСМОТР ТЕКСТА ДЛЯ РАССЫЛКИ'
    }


class Text_MailingUpdateView(UpdateView):
    model = Text_Mailing
    form_class = Text_MailingForm

    extra_context = {
        'title': 'РЕДАКТИРОВАНИЕ ТЕКСТА ДЛЯ РАССЫЛКИ'
    }


class Log_MailingListView(ListView):
    model = Log_Mailing
    form_class = Log_MailingForm

    extra_context = {
        'title': 'ПРОСМОТР ЛОГОВ'
    }

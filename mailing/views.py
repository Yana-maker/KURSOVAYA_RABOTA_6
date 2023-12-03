from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from mailing.forms import Text_MailingForm
from mailing.models import Text_Mailing


# Create your views here.


class ProductCreateView(CreateView):
    model = Text_Mailing
    form_class = Text_MailingForm
    success_url = reverse_lazy('main:home')

    extra_context = {
        'title': 'СОЗДАНИЕ РАССЫЛКИ'
    }


class ProductUpdateView(UpdateView):
    model = Text_Mailing
    success_url = reverse_lazy('main:update')

    extra_context = {
        'title': 'РЕДАКТИРОВАНИЕ РАССЫЛКИ'
    }


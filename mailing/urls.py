from django.urls import path

from catalog.apps import CatalogConfig
from mailing.views import MailingCreateView, MailingUpdateView, MailingListView

app_name = CatalogConfig.name

urlpatterns = [

    path('list/', MailingListView.as_view(template_name='mailing/text_mailing_list.html'), name='list'),
]

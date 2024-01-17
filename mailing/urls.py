from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingCreateView, MailingUpdateView, MailingListView, ClientCreateView, ClientListView, \
    ClientUpdateView, Text_MailingCreateView, Text_MailingListView, Text_MailingUpdateView

app_name = MailingConfig.name

urlpatterns = [

    path('create/', MailingCreateView.as_view(), name='create'),
    path('list/', MailingListView.as_view(), name='list'),
    path('edit/<int:pk>/', MailingUpdateView.as_view(), name='edit'),
    path('create/', Text_MailingCreateView.as_view(), name='create'),
    path('list/', Text_MailingListView.as_view(), name='list'),
    path('edit/<int:pk>/', Text_MailingUpdateView.as_view(), name='edit'),
    path('create/', ClientCreateView.as_view(), name='create'),
    path('list/', ClientListView.as_view(), name='list'),
    path('edit/<int:pk>/', ClientUpdateView.as_view(), name='edit'),
]

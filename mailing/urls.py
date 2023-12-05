from django.urls import path

from catalog.apps import CatalogConfig
from mailing.views import MailingCreateView, MailingUpdateView, MailingDetailView, MailingDeleteView
from catalog.models import Product

app_name = CatalogConfig.name

urlpatterns = [

    path('create/', MailingCreateView.as_view(), name='create'),
    path('view/<int:pk>/', MailingDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', MailingUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='delete'),
]

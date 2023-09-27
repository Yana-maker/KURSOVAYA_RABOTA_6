from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ContactsCreateView
from catalog.apps import CatalogConfig
from catalog.models import Product

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsCreateView.as_view(), name='contacts'),
    path('<int:pk>/catalog/', ProductDetailView.as_view(), name='product'),
]
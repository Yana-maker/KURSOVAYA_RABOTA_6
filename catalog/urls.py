from django.urls import path
from catalog.views import home, contacts, product
from catalog.apps import CatalogConfig
from catalog.models import Product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/catalog/', product, name='product'),
]
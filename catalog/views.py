from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from catalog.models import Product, Contacts
from catalog.forms import ProductForm, ContactsForm


# Create your views here.

class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'ГЛАВНАЯ'
    }


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': 'ПРОСМОТР ПРОДУКТА'
    }


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    extra_context = {
        'title': 'СОЗДАНИЕ ПРОДУКТА'
    }


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    extra_context = {
        'title': 'РЕЛАКТИРОВАНИЕ ПРОДУКТА'
    }


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')

    extra_context = {
        'title': 'УДАЛЕНИЕ ПРОДУКТА'
    }


def toggle_activity():
    pass


class ContactsCreateView(CreateView):
    model = Contacts
    form_class = ContactsForm
    success_url = reverse_lazy('catalog:home')
    extra_context = {
        "title": "КОНТАКТЫ"
    }


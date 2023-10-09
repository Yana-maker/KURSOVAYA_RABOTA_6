from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from catalog.models import Product, Contacts, Version
from catalog.forms import ProductForm, ContactsForm, VersionForm


# Create your views here.

class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'ГЛАВНАЯ'
    }

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        for product in context['object_list']:
            active_version = product.version_set.filter(is_current_version=True).first()
            if active_version:
                product.active_number_version = active_version.number_version
                product.active_name_version = active_version.name_version
            else:
                product.active_number_version = None
                product.active_name_version = None

        return context


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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        return context_data


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')

    extra_context = {
        'title': 'УДАЛЕНИЕ ПРОДУКТА'
    }



class ContactsCreateView(CreateView):
    model = Contacts
    form_class = ContactsForm
    success_url = reverse_lazy('catalog:home')
    extra_context = {
        "title": "КОНТАКТЫ"
    }



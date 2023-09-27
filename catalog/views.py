from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from catalog.models import Product, Contacts


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'ГЛАВНАЯ'
    }


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'



class ContactsCreateView(CreateView):
    model = Contacts
    fields = ('name', 'email', 'massage',)
    success_url = reverse_lazy('catalog:home')
    extra_context = {
        "title": "Контакты"
    }

    template_name = 'catalog/contacts.html'




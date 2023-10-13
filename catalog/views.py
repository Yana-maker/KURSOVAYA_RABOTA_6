from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from catalog.models import Product, Contacts, Version
from catalog.forms import ProductForm, ContactsForm, VersionForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context['formset'] = VersionFormSet(self.request.POST)
        else:
            context['formset'] = VersionFormSet()
        return context

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    extra_context = {
        'title': 'РЕДАКТИРОВАНИЕ ПРОДУКТА'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context['formset'] = VersionFormSet(self.request.POST)
        else:
            context['formset'] = VersionFormSet()
        return context

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


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

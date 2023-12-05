from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from catalog.models import Product, Contacts, Version
from catalog.forms import ProductForm, ContactsForm, VersionForm


# Create your views here.



class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product

    permission_required = 'catalog.view_product'
    extra_context = {
        'title': 'ГЛАВНАЯ'
    }


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Product
    permission_required = 'catalog.view_product'
    extra_context = {
        'title': 'ПРОСМОТР ПРОДУКТА'
    }




class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_product'
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
        self.object.owner_product = self.request.user
        self.object.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'
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

    def get_form(self, form_class=None):
        """
        Если у пользователя нет прав на редактирование поля удаляем его из формы.
        """
        form = super().get_form(form_class)
        if self.object.owner_product != self.request.user:
            product_fields = [f for f in form.fields.keys()]

            for field in product_fields:
                if not self.request.user.has_perm(f'catalog.{field}'):
                    del form.fields[field]
        return form



class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = 'catalog.delete_product'
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



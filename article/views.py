from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from article.models import Article
from pytils.translit import slugify


# Create your views here.

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ('title', 'text', 'preview')
    success_url = reverse_lazy('article:list')
    extra_context = {
        'title': 'СОЗДАНИЕ СТАТЬИ'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_art = form.save()
            new_art.slug = slugify(new_art.title)
            new_art.save()
        return super().form_valid(form)


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    extra_context = {
        'title': 'СТАТЬИ'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    extra_context = {
        'title': 'ИНФО И СТАТЬЕ'
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ('title', 'text', 'preview')
    extra_context = {
        'title': 'РЕДАКТИРОВАНИЕ СТАТЬИ'
    }

    def get_success_url(self):
        return reverse('article:view', args=[self.object.pk])

    def form_valid(self, form):
        if form.is_valid():
            new_art = form.save()
            new_art.slug = slugify(new_art.title)
            new_art.save()
        return super().form_valid(form)





class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('article:list')
    extra_context = {
        'title': 'УДАЛЕНИЕ СТАТЬИ'
    }

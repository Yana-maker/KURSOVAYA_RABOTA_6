from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from article.models import Article
from pytils.translit import slugify


# Create your views here.

class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'text', 'preview')
    success_url = reverse_lazy('article:list')
    extra_context = {
        'title': 'Создание статьи'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_art = form.save()
            new_art.slug = slugify(new_art.title)
            new_art.save()
        return super().form_valid(form)


class ArticleListView(ListView):
    model = Article
    extra_context = {
        'title': 'Статьи'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleDetailView(DetailView):
    model = Article
    extra_context = {
        'title': 'Инфо о статье'
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'text', 'preview')
    extra_context = {
        'title': 'Редактирование Статьи'
    }

    def get_success_url(self):
        return reverse('article:view', args=[self.object.pk])

    def form_valid(self, form):
        if form.is_valid():
            new_art = form.save()
            new_art.slug = slugify(new_art.title)
            new_art.save()
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('article:list')
    extra_context = {
        'title': 'Удаление статьи'
    }

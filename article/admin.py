from django.contrib import admin

from article.models import Article


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'preview', 'create_data', 'is_published', 'view_count',)
    list_filter = ('title',)
    search_fields = ('title',)
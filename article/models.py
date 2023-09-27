from django.db import models

NULLABLE = {'null': True, 'blank': True}

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    preview = models.ImageField(upload_to='article/', verbose_name='фото', **NULLABLE)
    text = models.CharField(max_length=500, verbose_name='содержимое')
    create_data = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    is_published = models.BooleanField(default=True, verbose_name='доступна ли для публикации')
    view_count = models.IntegerField(default=0, verbose_name='просмотры')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('title',)


from django.conf import settings
from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='название')
    category_description = models.CharField(max_length=150, verbose_name='описание')

    def __str__(self):
        return f'{self.category_name} - {self.category_description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='название')
    product_description = models.CharField(max_length=500, verbose_name='описание')
    product_image = models.ImageField(upload_to='product/', verbose_name='фото', **NULLABLE)
    product_category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='категория')
    product_price = models.IntegerField(verbose_name='цена')
    product_created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    product_updated_at = models.DateTimeField(auto_now=True, verbose_name="дата посл изменения")
    is_published = models.BooleanField(default=False, verbose_name="статус публикации")

    owner_product = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                                      verbose_name='добавил:')

    def __str__(self):
        return f"{self.product_name}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_price',)

        permissions = (

            ('set_product_description',
             'редактирование описания продукта'),
            ('set_product_category',
             'редактирование категории продукт'),
            ('set_product_price',
             'редактирования цены продукт'),
        )


class Contacts(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    email = models.EmailField(unique=True, verbose_name="Почта", **NULLABLE)
    massage = models.CharField(max_length=150, verbose_name="Краткое описание")

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ('name',)


class Version(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='название продукта')
    number_version = models.IntegerField(verbose_name='номер')
    name_version = models.CharField(max_length=150, verbose_name='название версии')
    is_current_version = models.BooleanField(default=True, verbose_name='признак версии')

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('product_name',)



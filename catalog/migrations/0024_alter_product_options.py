# Generated by Django 4.2.4 on 2023-11-29 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0023_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('product_price',), 'permissions': (('product_description', 'set product_description продукт'), ('product_category', 'set product_category продукт'), ('product_price', 'set product_price продукт')), 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]

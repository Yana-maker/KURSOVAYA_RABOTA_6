# Generated by Django 4.2.4 on 2023-11-28 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('product_price',), 'permissions': (('can_product_description', 'Can Product_description Posts'),), 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AlterModelOptions(
            name='version',
            options={'ordering': ('product_name',), 'verbose_name': 'версия', 'verbose_name_plural': 'версии'},
        ),
    ]
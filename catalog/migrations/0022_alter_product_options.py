# Generated by Django 4.2.4 on 2023-11-28 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('product_price',), 'permissions': (('set_product_description', 'set product_description Product'),), 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]
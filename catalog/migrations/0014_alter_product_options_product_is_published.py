# Generated by Django 4.2.4 on 2023-11-16 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_product_owner_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('product_price',), 'permissions': [('set_published', 'Can publish posts')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
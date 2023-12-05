import json

from django.core.management import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'category_name': 'фрукты', 'category_description': 'грущи, яблоки'},
            {'category_name': 'овощи', 'category_description': 'картошка, лук и тп'},
            {'category_name': 'бытовая химия', 'category_description': 'средства для мытья поля, кухонной утвари'},
            {'category_name': 'уход для тела', 'category_description': 'масло для тела, гели для души и тп'},
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )


        Category.objects.bulk_create(category_for_create)



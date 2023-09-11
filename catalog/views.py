from django.shortcuts import render
from catalog.models import Product

# Create your views here.

def home(request):
    object_list = Product.objects.all()
    context = {
        'object_list': object_list,
        "title": "Товары"
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('massage')
        print(f'{name} ({email}): {massage}')

    context = {
        "title": "Контакты"
    }
    return render(request, 'catalog/contacts.html', context)



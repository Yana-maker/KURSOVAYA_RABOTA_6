from django.shortcuts import render
from catalog.models import Product

# Create your views here.

def home(request):
    context = {
        'object_list': Product.objects.all(),
        "title": "Главная"
    }

    return render(request, 'catalog/home.html', context)

def product(request, pk):
    object_items = Product.objects.get(pk=pk)

    context = {
        'object_list': Product.objects.filter(pk=pk),
        "title": f"Товары {object_items.product_name}"
    }

    return render(request, 'catalog/product.html', context)



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



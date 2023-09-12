from django.core.paginator import Paginator
from django.shortcuts import render
from catalog.models import Product

# Create your views here.

def home(request):
    object_list = Product.objects.all()
    context = {
        'object_list': object_list,
        "title": "Главная"
    }
    return render(request, 'catalog/home.html', context)

def product(request):
    products_item = Product.objects.all()
    object_list = Product.objects.all()
    paginator = Paginator(products_item, 1)

    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)

    context = {
        'object_list': object_list,
        'page_obj': page_obj,
        "title": "Товары"
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



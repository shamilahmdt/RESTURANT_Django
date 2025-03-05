from django.shortcuts import render

from resturant.models import Category
from resturant.models import Menu

def index(request):
    categories = Category.objects.all()
    menu = Menu.objects.all()

    context = {
        'categories' : categories,
        'menu' : menu
    }

    return render(request, 'index.html' , context=context)

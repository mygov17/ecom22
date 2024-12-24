from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def category(request, foo):
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.object.filter(category=category)
        return render(request, 'core/category.html', {'products':products,'category':category})
    except:
        messages.success(request, ("There is no category like that"))
        return redirect('home')



def home(request):
    products = Product.objects.all()

    context = {'products':products}
    return render(request, 'core/home.html', context)

def product(request, pk):
    product = Product.objects.get(id=pk)

    context = {'product':product}
    return render(request, 'core/product.html', context)
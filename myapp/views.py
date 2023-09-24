from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def catalog(request):
    products = Product.objects.all()
    return render(request, 'myapp/catalog.html', {'products': products})

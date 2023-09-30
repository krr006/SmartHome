from django.shortcuts import render, get_object_or_404
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

def faq(request):
    return render(request, 'myapp/faq.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'myapp/product_detail.html', {'product': product})

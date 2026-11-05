
from django.shortcuts import render, get_object_or_404
from .models import Product


# Home page
def home(request):
    products = Product.objects.all()

    return render(request, 'store/home.html', {
        'products': products
    })


# Product details page
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    return render(request, 'store/product_detail.html', {
        'product': product
    })


from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Product
from .cart import Cart


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


# Add product to cart
@require_POST
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    cart = Cart(request)
    cart.add(product)

    return redirect('cart_detail')


# View shopping cart
def cart_detail(request):
    cart = Cart(request)

    return render(request, 'store/cart.html', {
        'cart': cart
    })


# Remove product from cart
@require_POST
def remove_from_cart(request, id):
    product = get_object_or_404(Product, id=id)

    cart = Cart(request)
    cart.remove(product)

    return redirect('cart_detail')

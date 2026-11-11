
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path(
        'product/<int:id>/',
        views.product_detail,
        name='product_detail'
    ),

    path('cart/', views.cart_detail, name='cart_detail'),

    path(
        'cart/add/<int:id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    path(
        'cart/remove/<int:id>/',
        views.remove_from_cart,
        name='remove_from_cart'
    ),
]

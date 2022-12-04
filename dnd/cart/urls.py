from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.cart_detail, name='cart_detail'),
    path(r'add/<int:pk>/', views.cart_add, name='cart_add'),
    path(r'remove/<int:pk>/', views.cart_remove, name='cart_remove'),
    path("buy/", views.buy_view, name="buy"),
]

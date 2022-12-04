from django.contrib import admin
from .models import CustomClient, Product, ProductsInCart

admin.site.register(CustomClient)
admin.site.register(Product)
admin.site.register(ProductsInCart)

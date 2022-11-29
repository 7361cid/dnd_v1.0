from django.urls import path
from .views import Signup, Login, Logout, UserPage, main_page, Shop, product_detail

urlpatterns = [
    path("signup/", Signup.as_view(), name="signup"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("shop/<int:pk>/", product_detail, name="product"),
    path("shop/", Shop.as_view(), name="shop"),
    path('user/<int:pk>/', UserPage.as_view(), name="user"),
    path("",   main_page, name="home"),
]

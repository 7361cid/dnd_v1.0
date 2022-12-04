from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.apps import apps
from .cart import Cart
from .forms import CartAddProductForm

Product = apps.get_model('client', 'Product')
ProductsInCart = apps.get_model('client', 'ProductsInCart')

@require_POST
def cart_add(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, id=pk)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart_detail.html', {'cart': cart})


def buy_view(request):
    """
    Логика покупки товара
    """
    cart = Cart(request)
    print(f"Log BUY VIEW {cart}")
    print(f"Log BUY VIEW {request.user}")
    print(f"Log BUY VIEW {request.user.money}")
    if request.user.money > cart.get_total_price():
        request.user.money = request.user.money - cart.get_total_price()
        request.user.save()
        for item in cart:
            print(f"Log BUY VIEW product {item} \n {item.keys()}")
            print(f'Log BUY VIEW user_pk {request.user.pk} {item["product"].pk} {type(request.user.pk)}')
            product_in_cart_object = ProductsInCart(user_pk=request.user.pk,
                                                    product_pk=item["product"].pk, count=item["quantity"])
            product_in_cart_object.save()
            print(f'Log BUY VIEW product_in_cart_object {product_in_cart_object}')
        cart.clear()
        context = {'cart':cart, 'bich': False}
    else:
        context = {'bich': True}
    return render(request, 'cart_detail.html', context)

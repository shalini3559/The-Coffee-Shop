from django.shortcuts import render,redirect
from .models import Coffee, CartItem





# Create your views here.
#def cart_home(request):
    #request.session['cart_id'] = 1
    #request.session['user'] = request.user.username
    #context = {

    #}
    #template = "cart/home.html"
   # return render(request, template, context)


def view_cart(request):
    template = "cart\cart.html"
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, template, {'cart_items': cart_items, 'total_price': total_price})
 
def add_to_cart(request, product_id):
    Coffee = Coffee.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(Coffee=Coffee, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')
 
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')

    

    
from django.urls import path
from .views import view_cart
from . import views 


app_name = "cart"

urlpatterns = [
    path('cartpage/',view_cart, name = "cartpage"),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
    
    
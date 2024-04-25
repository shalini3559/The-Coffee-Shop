from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name="home"),
# path('', views.CoffeeList.as_view(), name = "home"),
path('coffee/<int:pk>', views.ProdDetails.as_view(), name="coffee_details" )
]



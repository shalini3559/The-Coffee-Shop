from django.urls import path
from .views import UserRegisterView
# from .views import register_page, login_page,logOut,search_result

urlpatterns = [
   # path('register/', register_page, name = "register"),
    path('signup/',UserRegisterView.as_view(), name='register'),
   # path('logOut/', logOut, name="logOut")
  

]
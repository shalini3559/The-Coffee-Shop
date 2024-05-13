from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic 







# Create your views here.

def register_page(request):
    form = UserRegisterForm()
    context ={
        "title" : "register Page",
        "form"  : form
    }
    
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=True)
            user.set_password(user.password)
            user.save()
            return redirect('/login')
        else:
            return render(request,"register.html",context)
    return render(request,"register.html",context)


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
        

                      
                      
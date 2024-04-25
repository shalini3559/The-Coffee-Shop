from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader # helps load the template
from .models import Coffee

from django.views.generic import ListView, DetailView




# Create your views here.
def home(request):
    template = loader.get_template('home.html')
    coffees = Coffee.objects.all()
    context = {
        'coffee1': coffees
    }
    return HttpResponse(template.render(context, request))

def register(request):
    return HttpResponse("Hi this is a registeration page....!")
      

# class CoffeeList(ListView):
#     queryset = Coffee.objects.all()
#     template_name = "home.html"

    

class ProdDetails(DetailView):
    queryset = Coffee.objects.all()
    template_name = 'prod_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProdDetails, self).get_context_data(*args, **kwargs)
        return context 
    
    

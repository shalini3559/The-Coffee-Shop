from django.db import models
from BrewHaven.models import Coffee
from django.contrib.auth.models import User




# Create your models here



#class Cart(models.Model):
    #cart_id = models.CharField(max_length=255, blank=True)
    #coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #quantity = models.IntegerField(default=1)
    #totalprice = models.FloatField(default=0.0)
    #timestamp =  models.DateTimeField(auto_now_add = True)

    #class Meta:
       # db_table = 'cart'

class CartItem(models.Model):
    Coffee= models.ForeignKey(Coffee, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.quantity} x {self.Coffee.name}'

    
    

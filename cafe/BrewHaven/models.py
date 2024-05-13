from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Coffee(models.Model):
     name = models.CharField(max_length = 255)
     price = models.FloatField()
     quantity = models.IntegerField()
     img = models.ImageField(upload_to="coffees/", null=True)

#class CartItem(models.Model):
     #cartuser = models.ForeignKey(User, on_delete=models.CASCADE)
    # quantity = models.IntegerField()
     #item = models.ForeignKey(Coffee, on_delete=models.CASCADE)
     #total_price = models.FloatField()
     


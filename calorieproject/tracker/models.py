from django.db import models
from django.contrib.auth.models import User




class Cust(models.Model): # for any customers
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=25, null=True)
    email=models.CharField(max_length=50, null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)



class Category(models.Model): # the meal of the food
    meals=(
        ('breakfast','breakfast'),
        ('lunch','lunch'),
        ('dinner','dinner'),
        ('snacks','snacks'),
    )
    name=models.CharField(max_length=60, choices=meals)
    
    
    def __str__(self):
        return str(self.name)




class Item(models.Model): # for all food items 
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    carbohydrate = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    fats = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    protein = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    calorie=models.DecimalField(max_digits=5,decimal_places=2,default=0,blank=True)
    quantity = models.IntegerField(default=1,null=True,blank=True)

    def __str__(self):
        return str(self.name)



    

    
class UserFoodItem(models.Model):  # for associations and what the user has eaten
    cust=models.ManyToManyField(Cust, blank=True)
    food_item=models.ManyToManyField(Item)

    

    








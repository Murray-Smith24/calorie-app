from django.contrib import admin
from .models import *

# Register your models here.
class foodAdmin(admin.ModelAdmin):
    class Meta:
        model = Item
    list_display=['name']
    list_filter=['name']

admin.site.register(Cust)
admin.site.register(UserFoodItem)
admin.site.register(Category)
admin.site.register(Item, foodAdmin)
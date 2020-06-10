from django.contrib import admin
from .models import Quantity, Item, Inventory
# Register your models here.


admin.site.register(Item)
admin.site.register(Quantity)
admin.site.register(Inventory)
from django.contrib import admin
from restaurant.models import MyTopping, MyPizza

# Register your models here.
admin.site.register(MyPizza)
admin.site.register(MyTopping)
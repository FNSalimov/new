from django.contrib import admin
from .models import Dish, Order

class DishAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'price')

class OrderAdmin(admin.ModelAdmin):
	list_display = ('count', 'operator', 'time', 'restor_name')

admin.site.register(Dish, DishAdmin)
admin.site.register(Order, OrderAdmin)

from django.contrib import admin
from products.models import food, drinks, freshfood

@admin.register(food)
class food_admin(admin.ModelAdmin):
    list_display = ['name', 'price', 'kilos']

@admin.register(drinks)
class drinks_admin(admin.ModelAdmin):
    list_display = ['name', 'price', 'gallons']

@admin.register(freshfood)
class freshfood_admin(admin.ModelAdmin):
    list_display = ['name', 'price', 'kilos', 'rottendays']   
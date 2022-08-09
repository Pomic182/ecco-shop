
from django.contrib import admin
from django.urls import path
from products.views import create_food, create_freshfood, create_drinks, list_drinks, list_food, list_freshfood

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food_product/', create_food, name='food_product'),
    path('freshfood_product/', create_freshfood, name='freshfood_product'),
    path('drink_product/', create_drinks, name='drinks_product'),
    path('list_drinks/', list_drinks, name='list_drinks'),
    path('list_food/', list_food, name='list_food'),
    path('list_freshfood/', list_freshfood, name='list_freshfood'),
    

]

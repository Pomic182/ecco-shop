from ast import For
import contextlib
from contextvars import Context
from multiprocessing import context
from django.shortcuts import render, redirect
from products.models import food, freshfood, drinks
from products.forms import Formulario_productos, Formulario_drink, Formulario_freshfood



def create_food(request):
    
    if request.method == 'POST':
        form = Formulario_productos(request.POST)
        if form.is_valid():
            food.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                kilos = form.cleaned_data['kilos']
            )
            return redirect(list_food)
    #    food_product= food.objects.create(name='lata de durazno', price= 350, kilos= 0.500)
    #    context = {
    #        'food_product': food_product
    #    }
    elif request.method == 'GET':
        form = Formulario_productos()
        context = {'forms': form}
        return render(request, 'food_product.html', context=context)

def create_freshfood(request):
    

    freshfood_product= freshfood.objects.create(name='manzana', price= 50, kilos= 0.2, rottendays= 10)
    context = {
        'freshfood_product': freshfood_product
    }
    return render(request, 'freshfood_product.html', context=context)

def create_drinks(request):
    drinks_product= drinks.objects.create(name='fanta', price= 250, gallons= 0.2)
    context = {
        'drinks_product': drinks_product
    }
    return render(request, 'drinks_product.html', context=context)

    #    food_product= food.objects.create(name='lata de durazno', price= 350, kilos= 0.500)
    #    context = {
    #        'food_product': food_product
    #    }
 

def list_food(request):
    foods = food.objects.all()
    context = {
        'foods' : foods
    }
    return render(request, 'list_food.html', context=context)

def list_freshfood(request):
    freshfoods = freshfood.objects.all()
    context={
        'freshfoods' : freshfoods
    }
    return render(request, 'list_freshfood.html', context=context)

def list_drinks(request):
    refreshment = drinks.objects.all()
    context={
        'refreshment' : refreshment
    }
    return render(request, 'list_drinks.html', context=context)

def search_food(request):
    search = request.GET['search']
    foods = food.objects.filter(name__icontains=search)
    context = {'foods' : foods}
    return render (request, 'search_food.html/', context=context)


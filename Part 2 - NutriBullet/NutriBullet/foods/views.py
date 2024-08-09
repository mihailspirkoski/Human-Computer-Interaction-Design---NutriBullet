from django.shortcuts import render
from .models import Food
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
@login_required(login_url="/users/login/")
def foods_list(request, food_type):
    foods = Food.objects.all().filter(food_type = food_type)
    return render(request, 'foods/foods_list.html', {'foods':foods})

@login_required(login_url="/users/login/")
def food_page(request, food_type, slug):
    food = Food.objects.get(slug=slug)
    return render(request, 'foods/food_page.html', {'food':food})
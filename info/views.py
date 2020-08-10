from django.shortcuts import render
from .models import Restaurants
# Create your views here.

def home(request):
    rest = Restaurants.objects.all()
    return render(request, 'restaurant.html', {'restaurants': rest})


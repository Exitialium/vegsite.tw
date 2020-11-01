from django.shortcuts import render
from .models import Restaurants
from django.views import generic
# Create your views here.

class RestList(generic.ListView):
    queryset = Restaurants.objects.filter(status=1)
    template_name = 'index_in_English.html'

class RestDetail(generic.DetailView):
    model = Restaurants
    template_name = 'restaurant.html'




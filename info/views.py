from django.shortcuts import render
from .models import Restaurants
from django.views import generic
# Create your views here.

class RestList(generic.ListView):
    queryset = Restaurants
    template_name = 'index.html'

class RestDetail(generic.DetailView):
    model = Restaurants
    template_name = 'restaurants.html'




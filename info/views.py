from django.shortcuts import render
from .models import Restaurants
# Create your views here.

class RestList(generic.ListView):
    queryset = Restaurants.objects.order_by('rank')
    template_name = 'index.html'

class RestDetail(generic.DetailView):
    model = Restaurants
    template_name = 'restaurants.html'


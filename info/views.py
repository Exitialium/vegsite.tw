from django.shortcuts import render
from .models import Restaurants
# Create your views here.

class RestList(generic.ListView):
    queryset = Restaurants.objects.order_by('rank')
    template_name = 'index.html'

class RestDetail(generic.DetailView):
    model = Restaurants
    template_name = 'restaurants.html'
    queryset = Restaurants.order_by('rank')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Restaurants
    template_name = 'restaurant.html'



def home(request):
    rest = Restaurants.objects.all()
    return render(request, 'restaurant.html', {'restaurants': rest})


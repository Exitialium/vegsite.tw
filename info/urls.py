from . import views
from django.urls import path

urlpatterns = [
    path('', views.RestList.as_view(), name='home'),
    path('<slug:slug>/', views.RestDetail.as_view(), name='rest_detail'),
]
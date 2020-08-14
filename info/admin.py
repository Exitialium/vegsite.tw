from django.contrib import admin
from .models import Restaurants
# Register your models here.

class RestAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'status')
    list_filter = ("status",)
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Restaurants,RestAdmin)

from django.contrib import admin
from .models import CarsModel


@admin.register(CarsModel)
class CarsModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']

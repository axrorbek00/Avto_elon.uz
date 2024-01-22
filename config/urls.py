from django.contrib import admin
from django.urls import path
from home.views import CarsView
from rest_framework.routers import DefaultRouter

# routers = DefaultRouter()
# routers.register('cars/', CarsView, basename='cars/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', CarsView.as_view())
]
# ] + routers.urls

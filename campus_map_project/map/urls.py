from django.urls import path
from .views import map_view, save_location

urlpatterns = [
    path('', map_view, name='map'),
    path('save-location/', save_location, name='save_location'),
]

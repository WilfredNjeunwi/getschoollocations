from rest_framework import viewsets
from .models import CampusLocation
from .serializers import CampusLocationSerializer
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import CampusLocation

class CampusLocationViewSet(viewsets.ModelViewSet):
    queryset = CampusLocation.objects.all()
    serializer_class = CampusLocationSerializer



def map_view(request):
    return render(request, 'map/map.html')



def save_location(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        image = request.FILES.get('image')

        if name and latitude and longitude and image:
            location = CampusLocation(
                name=name,
                latitude=latitude,
                longitude=longitude,
                image=image
            )
            location.save()
            return JsonResponse({"message": "Location saved successfully!"}, status=200)
        else:
            return JsonResponse({"error": "Missing data"}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)

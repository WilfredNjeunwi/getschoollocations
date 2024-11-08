from rest_framework import serializers
from .models import CampusLocation

class CampusLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampusLocation
        fields = ['id', 'name', 'latitude', 'longitude', 'image']

from rest_framework import serializers
from .models import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = [
            'id',
            'title',
            'description',
            'genus',
            'watering_info',
            'soil_type'
        ]
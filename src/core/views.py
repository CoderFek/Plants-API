from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Plant
from .serializers import PlantSerializer


class PlantList(generics.ListCreateAPIView):
    
    serializer_class = PlantSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Plant.objects.filter(owner=self.request.user)

        


class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = PlantSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Plant.objects.filter(owner=self.request.user)
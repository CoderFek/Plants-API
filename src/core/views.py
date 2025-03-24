from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from .models import Plant
from .serializers import PlantSerializer


class PlantList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    
    serializer_class = PlantSerializer
    permission_classes = [IsAuthenticated]

    """
    Return plant list
    """

    def get_queryset(self):
        return Plant.objects.filter(owner=self.request.user)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs) 

    """
    Create a new plant
    """

    def perform_create(self, serializer):   # overriding perform_create
        serializer.save(owner=self.request.user)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        


class PlantDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    
    serializer_class = PlantSerializer
    permission_classes = [IsAuthenticated]

    """
    Get plant details
    """

    def get_queryset(self):
        return Plant.objects.filter(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    

    """
    Update lant details
    """
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

    """
    Delete plant
    """
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
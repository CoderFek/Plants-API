from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Plant
from .serializers import PlantSerializer

# Create your views here.

# @api_view(['GET'])
# def plant_list_view(request):
#     user = request.user
    
#     if user.is_authenticated:
#         instance = Plant.objects.all()
#         data = {}
        
#         if instance:
#             data = PlantSerializer(instance, many=True).data
#         return Response(data)
        
#     return Response({"error": "Authentication Error"}, status=401)


class PlantList(APIView):
    '''
    Return plant list
    '''
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        
        plants = Plant.objects.filter(owner=self.request.user)
        data = PlantSerializer(plants, many=True).data
        return Response(data)
        

    '''
    Create a new plant
    '''
    def post(self, request, format=None):
        
        new_plant = PlantSerializer(data=request.data)
        if new_plant.is_valid():
            new_plant.save(owner=self.request.user)   # save to db
            return Response({"success": "Plant added"}, status=201)
        return Response(new_plant.errors, status=400)


class PlantDetail(APIView):
    permission_classes = [IsAuthenticated]

    '''
    Get plant details
    '''
    def get(self, request, pk, format=None):
        plant = get_object_or_404(Plant, pk=pk, owner=self.request.user)
        data = PlantSerializer(plant).data
        return Response(data, status=200)
    

    '''
    Update lant details
    '''
    def put(self, request, pk, format=None):
        plant = get_object_or_404(Plant, pk=pk, owner=self.request.user)
        data = PlantSerializer(plant, data=request.data, partial=True)
        if data.is_valid():
            data.save(owner=plant.owner)
            return Response({"success": "Plant Updated"}, status=200)
        return Response(data.errors, status=400)
    

    '''
    Delete plant
    '''
    def delete(self, request, pk, format=None):
        plant = get_object_or_404(Plant, pk=pk, owner=self.request.user)
        plant.delete()
        return Response({"success": "Plant deleted"}, status=204)
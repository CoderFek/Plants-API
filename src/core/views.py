from rest_framework import generics, authentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Plant, CachePlant
from .serializers import PlantSerializer
import requests
from django.conf import settings
from slugify import slugify


API_KEY = settings.PERENUAL_ACCESS_KEY


class PlantList(generics.ListCreateAPIView):
    
    serializer_class = PlantSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication
    ]

    def get_queryset(self):
        return Plant.objects.filter(owner=self.request.user)
    
    def create(self, request, *args, **kwargs):
        raw_name = request.data.get("title", "")
        plant_name = raw_name.strip().title()

        if not plant_name:
            return Response({"error": "Plant name is required."}, status=400)

        # Check if the plant already exists for the user
        if Plant.objects.filter(owner=request.user, title__iexact=plant_name).exists():
            return Response({"error": "You already have this plant saved."}, status=400)

        # Try to fetch from cache (global)
        cached = CachePlant.objects.filter(title__iexact=plant_name).first()

        if cached:
            genus = cached.genus
            description = cached.description
            soil_type = cached.soil_type
            watering = cached.watering_info
        else:
            # Fetch from Perenual API
            api_key = API_KEY
            url = f"https://perenual.com/api/species-list?key={api_key}&q={plant_name}"

            try:
                response = requests.get(url)
                response.raise_for_status()
                if not response.text.strip():
                    return Response({"error": "Empty response from species list API."}, status=500)
                data = response.json()
            except (requests.RequestException, ValueError) as e:
                return Response({"error": f"Failed to fetch or parse species list: {str(e)}"}, status=500)

            if not data.get("data"):
                return Response({"error": "No plant details found."}, status=404)

            plant_id = data["data"][0]["id"]

            # Now fetch detailed plant info
            detail_url = f"https://perenual.com/api/species/details/{plant_id}?key={api_key}"

            try:
                detail_response_raw = requests.get(detail_url)
                detail_response_raw.raise_for_status()
                if not detail_response_raw.text.strip():
                    return Response({"error": "Empty response from species detail API."}, status=500)
                detail_response = detail_response_raw.json()
            except (requests.RequestException, ValueError) as e:
                return Response({"error": f"Failed to fetch or parse species details: {str(e)}"}, status=500)

            genus = detail_response.get("genus", "") or ""
            description = detail_response.get("description", "") or ""
            soil_type = detail_response.get("soil", "") or ""
            watering = detail_response.get("watering", "") or ""

            # Save to cache
            CachePlant.objects.create(
                title=plant_name,
                genus=genus,
                description=description,
                soil_type=soil_type,
                watering_info=watering
            )

        # Save plant for the user
        plant = Plant.objects.create(
            owner=request.user,
            title=plant_name,
            genus=genus,
            description=description,
            soil_type=soil_type,
            watering_info=watering
        )

        return Response(PlantSerializer(plant).data, status=201)



        


class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = PlantSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication
    ]

    def get_queryset(self):
        return Plant.objects.filter(owner=self.request.user)
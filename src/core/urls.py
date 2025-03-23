from django.urls import path
from .views import PlantList, PlantDetail

urlpatterns = [
    path('plants/', PlantList.as_view()),
    path('plants/<int:pk>/', PlantDetail.as_view()),

]
from django.urls import path
from .views import PlantList, PlantDetail
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('plants/', PlantList.as_view()),
    path('plants/<int:pk>/', PlantDetail.as_view()),
    path('auth/', obtain_auth_token),

]
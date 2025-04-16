from django.urls import path
from .views import PlantList, PlantDetail, CustomTokenObtainPairView, CustomTokenRefreshView, CustomTokenVerifyView, LogoutView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('plants/', PlantList.as_view()),
    path('plants/<int:pk>/', PlantDetail.as_view()),

    path('jwt/create/', CustomTokenObtainPairView.as_view()),
    path('jwt/refresh/', CustomTokenRefreshView.as_view()),
    path('jwt/verify/', CustomTokenVerifyView.as_view()),
    path('logout/', LogoutView.as_view()),


]
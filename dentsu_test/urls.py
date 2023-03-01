from django.urls import path, include
from django .models import Count
from rest_framework import routers, serializers, viewsets

#here isour routers
router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
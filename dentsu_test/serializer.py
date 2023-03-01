from rest_framework import routers, serializers, viewsets
from .models import Count

# serializing

class CountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Count
        fields = ['service_name', 'status_code', 'start_date', 'end_date']

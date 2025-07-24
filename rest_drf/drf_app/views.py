from django.shortcuts import render
from drf_app.models import TwoWheelar
from drf_app.serializers import TwoWheelSer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class TwoWheelarViewSet(ModelViewSet):
    queryset = TwoWheelar.objects.all()
    serializer_class = TwoWheelSer

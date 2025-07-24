from drf_app.models import TwoWheelar
from rest_framework.serializers import ModelSerializer

class TwoWheelSer(ModelSerializer):
    class Meta:
        model = TwoWheelar
        fields = '__all__'

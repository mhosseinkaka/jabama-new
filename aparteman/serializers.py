from rest_framework.serializers import ModelSerializer
from aparteman.models import Place

class ApartemanListSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
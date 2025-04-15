from rest_framework.serializers import ModelSerializer, StringRelatedField
from colbe.models import Place

class ColbeListSerializer(ModelSerializer):
    user = StringRelatedField()
    owner = StringRelatedField()
    class Meta:
        model = Place
        fields = ['name', 'user', 'owner', 'location']

class ColbeSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

from rest_framework.serializers import ModelSerializer, StringRelatedField
from aparteman.models import Place

class ApartemanListSerializer(ModelSerializer):
    user = StringRelatedField()
    owener = StringRelatedField()
    class Meta:
        model = Place
        fields = ['name', 'user', 'owner']

class ApartemanSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

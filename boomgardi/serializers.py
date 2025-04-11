from rest_framework.serializers import ModelSerializer
from boomgardi.models import Place


class BoomgardiSerializer(ModelSerializer):

    class Meta:
        model = Place
        fields = '__all__'
        read_only_feilds= ['creator']
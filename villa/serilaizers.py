from rest_framework.serializers  import ModelSerializer
from villa.models import Villa

class VillaSerializer (ModelSerializer):
    class Meta :
        model = Villa 
        fields = '__all__'



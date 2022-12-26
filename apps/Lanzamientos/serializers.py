from rest_framework import serializers
from .models import Lanzamiento

class LanzamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lanzamiento
        fields = '__all__'

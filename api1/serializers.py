from rest_framework import serializers
from .models import Pais

class PaisSerializador(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('nombre', 'moneda')
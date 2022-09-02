from rest_framework import serializers
from termometriaV2.models import SiloV2

class SiloV2Serializer(serializers.ModelSerializer):
    class Meta:
        model = SiloV2
        fields = ['id', 'codigo_pacote', 'dados_pacote']
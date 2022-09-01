from rest_framework import serializers
from termometriaV1.models import SiloV1

class SiloV1Serializer(serializers.ModelSerializer):
    class Meta:
        model = SiloV1
        fields = ['id', 'codigo_pacote', 'dados_pacote']
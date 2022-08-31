from rest_framework import serializers
from termometriaV1.models import SiloV1, SecHorimetros

class SiloV1Serializer(serializers.ModelSerializer):
    class Meta:
        model = SiloV1
        fields = ['id', 'codigo_pacote', 'dados_pacote']


class SecHorimetrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecHorimetros
        fields = ['id', 'idEquipamento', 'dataHora', 'horasVent', 'minutosVent', 'horasDescarga', 'minutosDescarga', 'horasAspiracao', 'minutosAspiracao', 'horasAlimQueim', 'minutosAlimQueim', 'dtUltLimpezaPeriodica', 'dtUltEqualizDesc' ]
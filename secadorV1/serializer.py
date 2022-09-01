from rest_framework import serializers
from secadorV1.models import SecHorimetros

class SecHorimetrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecHorimetros
        fields = ['id', 'idEquipamento', 'dataHora', 'horasVent', 'minutosVent', 'horasDescarga', 'minutosDescarga', 'horasAspiracao', 'minutosAspiracao', 'horasAlimQueim', 'minutosAlimQueim', 'dtUltLimpezaPeriodica', 'dtUltEqualizDesc' ]
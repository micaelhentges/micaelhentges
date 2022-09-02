from rest_framework import serializers
from termometriaV1.models import SiloV1, SASAeracao, SASEstacao, SASEventos, SASPendulos, SASTermometria

class SiloV1Serializer(serializers.ModelSerializer):
    class Meta:
        model = SiloV1
        fields = ['id', 'codigo_pacote', 'dados_pacote']


class SASAeracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SASAeracao
        fields = ['id', 'idEquipamento', 'dataHora', 'horasAeraDiaria', 'potenciaTotalAera', 'potenciaTotalDia', 'valorKwh', 'valorConsumidoDia', 'valorConsumidoTotal', 'manualVentilador1', 'autoVentilador1', 'manualVentilador2', 'autoVentilador2', 'statusMotorV1', 'statusMotorV2', 'horasTotalV1', 'horasTotalV2', 'horasTotalAutoV1', 'horasTotalAutoV2', 'layoutSilo']

class SASEstacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SASEstacao
        fields = ['id', 'idEquipamento','dataHora','tempExterna', 'umidadeExterna', 'aerador', 'manual', 'sensorChuva', 'tempPlenum', 'umidadePlenum', 'layoutSilo']

class SASEventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = SASEventos
        fields = ['id', 'codigo_pacote', 'dados_pacote']


class SASPendulosSerializer(serializers.ModelSerializer):
    class Meta:
        model = SASPendulos
        fields = ['id', 'idTermometria', 'idEquipamento', 'dataHora', 'nPendulo', 'temperaturas', 'nivel']


class SASTermometriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SASTermometria
        fields = ['id', 'idTermometria', 'idEquipamento', 'dataHora', 'horasV1', 'horasAutoV1', 'horasDiariaV1', 'horasV2', 'horasAutoV2', 'horasDiariaV2', 'tempMedSilo', 'tempTopo', 'statusPrograma', 'modoTrocaPrograma', 'produto', 'programa', 'pontoQuenteAtivo', 'tempMaxPontoQuente', 'tempExterna', 'umidExterna', 'volumeSilo', 'nivelSilo', 'nivelLateral', 'nivelInterm', 'nivelCentral', 'dataNivel', 'dataCreate', 'progLivreUmidRelatMax', 'progLivreUmidRelatMin', 'progLivreTempAmbMax', 'progLivreTempAmbMin', 'progLivreLimiteHorasAera', 'progSecUmidEquilBase', 'progSecUmidEquilTopo', 'progSecUmidPretGrao', 'progResfDifTemp', 'progResfUmidEqMin', 'progResfTempPretend', 'progConsUmidObjGrao', 'progConsTempObjGrao', 'layoutSilo']
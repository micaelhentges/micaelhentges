from django.db import models

# Create your models here.
class SiloV1(models.Model):
    codigo_pacote = models.CharField(max_length=50)
    dados_pacote  = models.CharField(max_length=10000)

    def __str__(self) -> str:
        return self.codigo_pacote

class SASAeracao(models.Model):
    idEquipamento       = models.IntegerField(blank=True, null=True)
    dataHora            = models.DateTimeField(blank=True, null=True)
    horasAeraDiaria     = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    potenciaTotalAera   = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    potenciaTotalDia    = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    valorKwh            = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    valorConsumidoDia   = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    valorConsumidoTotal = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    manualVentilador1   = models.IntegerField(blank=True, null=True)
    autoVentilador1     = models.IntegerField(blank=True, null=True)
    manualVentilador2   = models.IntegerField(blank=True, null=True)
    autoVentilador2     = models.IntegerField(blank=True, null=True)
    statusMotorV1       = models.IntegerField(blank=True, null=True)
    statusMotorV2       = models.IntegerField(blank=True, null=True)
    horasTotalV1        = models.IntegerField(blank=True, null=True)
    horasTotalV2        = models.IntegerField(blank=True, null=True)
    horasTotalAutoV1    = models.IntegerField(blank=True, null=True)
    horasTotalAutoV2    = models.IntegerField(blank=True, null=True)
    layoutSilo          = models.IntegerField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.idEquipamento

class SASEstacao(models.Model):
    idEquipamento  = models.IntegerField(blank=True, null=True)
    dataHora       = models.DateTimeField(blank=True, null=True)
    tempExterna    = models.IntegerField(blank=True, null=True)
    umidadeExterna = models.IntegerField(blank=True, null=True)
    aerador        = models.IntegerField(blank=True, null=True)
    manual         = models.IntegerField(blank=True, null=True)
    sensorChuva    = models.IntegerField(blank=True, null=True)
    tempPlenum     = models.IntegerField(blank=True, null=True)
    umidadePlenum  = models.IntegerField(blank=True, null=True)
    layoutSilo     = models.IntegerField(blank=True, null=True)
        
    def __str__(self) -> str:
        return self.idEquipamento

class SASEventos(models.Model):
    idEquipamento = models.IntegerField(blank=True, null=True)
    dataHora      = models.DateTimeField(blank=True, null=True)
    evento        = models.IntegerField(blank=True, null=True)
            
    def __str__(self) -> str:
        return self.idEquipamento

class SASPendulos(models.Model): # Ver modo de pegar o id da termometria 
    idTermometria = models.IntegerField(blank=True, null=True)
    idEquipamento = models.IntegerField(blank=True, null=True)
    dataHora      = models.DateTimeField(blank=True, null=True)
    nPendulo      = models.IntegerField(blank=True, null=True)
    temperaturas  = models.CharField(max_length=100)
    nivel         = models.IntegerField(blank=True, null=True)
            
    def __str__(self) -> str:
        return self.idEquipamento


class SASTermometria(models.Model):
    idTermometria            = models.IntegerField(blank=True, null=True) # Código da termometria deve ser enviado junto para poder fazer ligação com os pendulos
    idEquipamento            = models.IntegerField(blank=True, null=True)
    dataHora                 = models.DateTimeField(blank=True, null=True)
    horasV1                  = models.IntegerField(blank=True, null=True)
    horasAutoV1              = models.IntegerField(blank=True, null=True)
    horasDiariaV1            = models.IntegerField(blank=True, null=True)
    horasV2                  = models.IntegerField(blank=True, null=True)
    horasAutoV2              = models.IntegerField(blank=True, null=True)
    horasDiariaV2            = models.IntegerField(blank=True, null=True)
    tempMedSilo              = models.IntegerField(blank=True, null=True)
    tempTopo                 = models.IntegerField(blank=True, null=True)
    statusPrograma           = models.IntegerField(blank=True, null=True)
    modoTrocaPrograma        = models.IntegerField(blank=True, null=True)
    produto                  = models.IntegerField(blank=True, null=True)
    programa                 = models.IntegerField(blank=True, null=True)
    pontoQuenteAtivo         = models.IntegerField(blank=True, null=True)
    tempMaxPontoQuente       = models.IntegerField(blank=True, null=True)
    tempExterna              = models.IntegerField(blank=True, null=True)
    umidExterna              = models.IntegerField(blank=True, null=True)
    volumeSilo               = models.IntegerField(blank=True, null=True)
    nivelSilo                = models.IntegerField(blank=True, null=True)
    nivelLateral             = models.IntegerField(blank=True, null=True)
    nivelInterm              = models.IntegerField(blank=True, null=True)
    nivelCentral             = models.IntegerField(blank=True, null=True)
    dataNivel                = models.DateTimeField(blank=True, null=True)
    dataCreate               = models.DateTimeField(blank=True, null=True)
    progLivreUmidRelatMax    = models.IntegerField(blank=True, null=True)
    progLivreUmidRelatMin    = models.IntegerField(blank=True, null=True)
    progLivreTempAmbMax      = models.IntegerField(blank=True, null=True)
    progLivreTempAmbMin      = models.IntegerField(blank=True, null=True)
    progLivreLimiteHorasAera = models.IntegerField(blank=True, null=True)
    progSecUmidEquilBase     = models.IntegerField(blank=True, null=True)
    progSecUmidEquilTopo     = models.IntegerField(blank=True, null=True)
    progSecUmidPretGrao      = models.IntegerField(blank=True, null=True)
    progResfDifTemp          = models.IntegerField(blank=True, null=True)
    progResfUmidEqMin        = models.IntegerField(blank=True, null=True)
    progResfTempPretend      = models.IntegerField(blank=True, null=True)
    progConsUmidObjGrao      = models.IntegerField(blank=True, null=True)
    progConsTempObjGrao      = models.IntegerField(blank=True, null=True)
    layoutSilo               = models.IntegerField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.idEquipamento
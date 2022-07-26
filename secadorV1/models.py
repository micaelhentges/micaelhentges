from django.db import models

class SecHorimetros(models.Model):
    idEquipamento = models.IntegerField(blank=True, null=True)
    dataHora              = models.DateTimeField(blank=True, null=True)
    horasVent             = models.IntegerField(blank=True, null=True)
    minutosVent           = models.IntegerField(blank=True, null=True)
    horasDescarga         = models.IntegerField(blank=True, null=True)
    minutosDescarga       = models.IntegerField(blank=True, null=True)
    horasAspiracao        = models.IntegerField(blank=True, null=True)
    minutosAspiracao      = models.IntegerField(blank=True, null=True)
    horasAlimQueim        = models.IntegerField(blank=True, null=True)
    minutosAlimQueim      = models.IntegerField(blank=True, null=True)
    dtUltLimpezaPeriodica = models.DateTimeField(blank=True, null=True)
    dtUltEqualizDesc      = models.DateTimeField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.idEquipamento
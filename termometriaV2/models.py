from django.db import models

# Create your models here.
class SiloV2(models.Model):
    codigo_pacote = models.CharField(max_length=50)
    dados_pacote  = models.CharField(max_length=10000)

    def __str__(self) -> str:
        return self.codigo_pacote
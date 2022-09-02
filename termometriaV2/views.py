from rest_framework import viewsets
from termometriaV2.models import SiloV2
from termometriaV2.serializer import SiloV2Serializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class SilosV2ViewSet(viewsets.ModelViewSet):
    """Exibindo todos os silos"""
    queryset = SiloV2.objects.all()
    serializer_class = SiloV2Serializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
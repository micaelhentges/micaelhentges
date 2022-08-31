from rest_framework import viewsets
from termometriaV1.models import SiloV1, SecHorimetros
from termometriaV1.serializer import SiloV1Serializer, SecHorimetrosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class SilosV1ViewSet(viewsets.ModelViewSet):
    """Exibindo todos os silos"""
    queryset = SiloV1.objects.all()
    serializer_class = SiloV1Serializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class SecHorimetrosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os silos"""
    queryset = SecHorimetros.objects.all()
    serializer_class = SecHorimetrosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
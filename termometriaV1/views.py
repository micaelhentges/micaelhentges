from rest_framework import viewsets
from termometriaV1.models import SiloV1, SASAeracao, SASEstacao, SASEventos, SASPendulos, SASTermometria
from termometriaV1.serializer import SiloV1Serializer, SASAeracaoSerializer, SASEstacaoSerializer, SASEventosSerializer, SASPendulosSerializer, SASTermometriaSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class SilosV1ViewSet(viewsets.ModelViewSet):
    """Exibindo todos os silos"""
    queryset = SiloV1.objects.all()
    serializer_class = SiloV1Serializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class SASAeracaoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os silos"""
    queryset = SASAeracao.objects.all()
    serializer_class = SASAeracaoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class SASEstacaoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os silos"""
    queryset = SASEstacao.objects.all()
    serializer_class = SASEstacaoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class SASEventosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os silos"""
    queryset = SASEventos.objects.all()
    serializer_class = SASEventosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class SASPendulosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os silos"""
    queryset = SASPendulos.objects.all()
    serializer_class = SASPendulosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class SASTermometriaViewSet(viewsets.ModelViewSet):
    """Exibindo todos os silos"""
    queryset = SASTermometria.objects.all()
    serializer_class = SASTermometriaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]                
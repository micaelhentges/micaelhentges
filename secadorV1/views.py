from rest_framework import viewsets
from secadorV1.models import SecHorimetros
from secadorV1.serializer import SecHorimetrosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class SecHorimetrosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os silos"""
    queryset = SecHorimetros.objects.all()
    serializer_class = SecHorimetrosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
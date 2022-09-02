"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from termometriaV1.views import SilosV1ViewSet, SASAeracaoViewSet, SASEstacaoViewSet, SASEventosViewSet, SASPendulosViewSet, SASTermometriaViewSet
from termometriaV2.views import SilosV2ViewSet
from secadorV1.views import SecHorimetrosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('silosV1', SilosV1ViewSet, basename='Silos V1')
router.register('SASAeracao', SASAeracaoViewSet, basename='Temometria V1 Aeracao')
router.register('SASEstacao', SASEstacaoViewSet, basename='Temometria V1 Estacao')
router.register('SASEventos', SASEventosViewSet, basename='Temometria V1 Eventos')
router.register('SASPendulos', SASPendulosViewSet, basename='Temometria V1 Pendulos')
router.register('SASTermometria', SASTermometriaViewSet, basename='Temometria V1 Termometria')

router.register('silosV2', SilosV2ViewSet, basename='Silos V2')
router.register('SecHorimetros', SecHorimetrosViewSet, basename='SecHorimetros')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

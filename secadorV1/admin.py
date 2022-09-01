from django.contrib import admin
from secadorV1.models import SecHorimetros

class SecHorimetros2(admin.ModelAdmin):
    list_display = ('id','idEquipamento', 'dataHora')
    list_display_links = ('id','idEquipamento', 'dataHora')
    search_fields = ('idEquipamento',)
    list_per_page = 20

admin.site.register(SecHorimetros, SecHorimetros2)
from django.contrib import admin
from termometriaV2.models import SiloV2

# Register your models here.
class SilosV2(admin.ModelAdmin):
    list_display = ('id','codigo_pacote', 'dados_pacote')
    list_display_links = ('id','codigo_pacote')
    search_fields = ('id',)
    list_per_page = 20

admin.site.register(SiloV2, SilosV2)

from django.contrib import admin
from termometriaV1.models import SiloV1

# Register your models here.
class SilosV1(admin.ModelAdmin):
    list_display = ('id','codigo_pacote', 'dados_pacote')
    list_display_links = ('id','codigo_pacote')
    search_fields = ('id',)
    list_per_page = 20

admin.site.register(SiloV1, SilosV1)
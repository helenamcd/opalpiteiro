from django.contrib import admin

from equipes.models import Equipe

class EquipeAdmin(admin.ModelAdmin):
    """
    Admin customizado para as equipes
    """
    list_display = ('sigla', 'nome',)

# Register your models here.
admin.site.register(Equipe, EquipeAdmin)
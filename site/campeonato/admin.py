#coding:utf-8
from django.contrib import admin

from campeonato.models import Campeonato, Fase, Grupo, TabelaGrupo, Rodada, Jogo

class GrupoInline(admin.StackedInline):
    """
        Inline para grupos. Para ser utilizado dentro do cadastro de Fases
    """
    model = Grupo
    extra = 1
    
class FaseAdmin(admin.ModelAdmin):
    """
        Admin para a fase de um campeonato
    """
    inlines = [
        GrupoInline,
    ]
    
    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + ('nome', 'campeonato',)
        
class FaseInline(admin.StackedInline):
    """
        Inline de Fases para um campeonato
    """
    model = Fase
    extra = 1
    
class CampeonatoAdmin(admin.ModelAdmin):
    """
        Admin para os campeonatos
    """
    inlines = [
        FaseInline,
    ]
    
class RodadaInline(admin.StackedInline):
    """
        Inline de Rodada para um grupo
    """
    
    model = Rodada
    extra = 1
    
class TabelaGrupoInline(admin.TabularInline):
    """
        Inline da Tabela do grupo
    """
    
    model = TabelaGrupo
    extra = 2
    
class GrupoAdmin(admin.ModelAdmin):
    """
        Admin para um grupo
    """    

    inlines = [RodadaInline, TabelaGrupoInline]
    
    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + ('fase', 'nome')


class JogoInline(admin.TabularInline):
    """
        Inline para os jogos, que será incluido no Admin da Rodada
    """
    
    model = Jogo
    extra = 1
    
class RodadaAdmin(admin.ModelAdmin):
    """
        Admin para as rodadas
    """
    inlines = [
        JogoInline
    ]
    
    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + ('grupo', 'nome')
    
    
    
admin.site.register(Campeonato, CampeonatoAdmin)
admin.site.register(Fase, FaseAdmin)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Rodada, RodadaAdmin)
#admin.site.register(Jogo)
#admin.site.register(TabelaGrupo)
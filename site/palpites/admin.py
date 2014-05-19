from django.contrib import admin
from palpites.models import Palpite

class PalpiteAdmin(admin.ModelAdmin):
    
    list_display = ['__unicode__', 'jogo', 'pontos', 'data', 'usuario']

# Register your models here.
admin.site.register(Palpite, PalpiteAdmin)
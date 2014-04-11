#coding:utf-8

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from usuarios.forms import FormAlterarUsuario, FormCriarUsuario
from usuarios.models import Usuario


class UsuarioAdmin(UserAdmin):
    """
    Classe admin para o usuario
    """
    form = FormAlterarUsuario
    add_form = FormCriarUsuario

    # Itens para exibição na lista de usuarios
    list_display = ('email', 'nome', 'telefone')
    list_filter = ('is_admin',)
    fieldsets = (
        ('Dados de acesso', {'fields': ('email', 'password', 'is_active')}),
        ('Dados Pessoais', {'fields': ('nome','telefone', 'apelido')}),
        ('Permissões', {'fields': ('is_admin',)}),
    )
    
    # Este fieldset só existe para o user do admin. Ao adicionar, ele só irá usar estes campos
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'telefone', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Registra o admin
admin.site.register(Usuario, UsuarioAdmin)

# Remove a parte de grupos do Django, não será necessária nesse site
admin.site.unregister(Group)
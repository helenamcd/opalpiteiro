#coding:utf-8

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group

from usuarios.models import Usuario


class FormCriarUsuario(forms.ModelForm):
    """
        Form para a criação de usuários
    """
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmação de senha", widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('email', 'nome', 'telefone')

    def clean_password2(self):
        """
        Valida se a 'password2' tem o mesmo valor de 'password1'
        """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não se equivalem")
        return password2

    def save(self, commit=True):
        """
        Salva o usuário
        """
        usuario = super(FormCriarUsuario, self).save(commit=False)
        usuario.set_password(self.cleaned_data["password1"])
        if commit:
            usuario.save()
        return usuario


class FormAlterarUsuario(forms.ModelForm):
    """
    Form para edição de usuários. O campo da senha é excluído
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ('email', 'nome', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        """Retorna a senha original"""
        return self.initial["password"]


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
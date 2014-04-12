#coding:utf-8

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

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
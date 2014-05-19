#coding:utf-8
from datetime import datetime

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from usuarios.managers import UsuarioManager


class Usuario(AbstractBaseUser):
    """
    Esta classe representa um usuario customizado para aplicação, substituindo o usuário padrão do Django.    
    """
    
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
    
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length = 255)
    apelido = models.CharField(max_length = 50, blank = True, null = True, default = "")
    telefone = models.CharField(max_length = 15)
    is_active = models.BooleanField("Ativo", default = False)
    is_admin = models.BooleanField("Administrador", default = False)    
    dataCadastro = models.DateTimeField(default = datetime.now())
    
    # Define o 'manager' para esta classe
    objects = UsuarioManager()
    
    # Indica que este campo será o identificador do usuário, ou seja, o que ele usará para fazer login
    USERNAME_FIELD = "email"
    
    # Campos obrigatórios pra criar um usuário
    REQUIRED_FIELDS = ['nome', 'telefone']
    
    
    # Métodos requeridos pelo Django
    def get_full_name(self):
        """
        Nome longo, devolve o nome do usuario
        """
        return self.nome
    
    def get_short_name(self):
        """
        Nome curto, devolve o apelido, caso exista. Caso não exista, devolve o nome longo
        """
        if self.apelido != "" and self.apelido is not None:
            return self.apelido
        else:
            return self.get_full_name()
        
    def has_perm(self, perm, obj = None):
        """
        Se o usuário tem permissões para determinada operação
        """
        return self.is_admin
    
    def has_module_perms(self, app_label):
        """
        Este usuário tem permissão para app_label ?
        """
        return self.is_admin
        
    @property
    def is_staff(self):
        """
        Método utilizado pelo admin para saber se o usuário faz parte da 'equipe'.
        Se o usuário é admin, então ele faz parte da equipe ;)
        """
        return self.is_admin
    
    # Métodos de negócio

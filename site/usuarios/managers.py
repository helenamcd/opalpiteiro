#coding:utf-8
'''
Created on 18/05/2014

@author: Lázaro
'''
from django.contrib.auth.models import BaseUserManager


class UsuarioManager(BaseUserManager):
    """
    Manager para o usuário customizado, pois não estaremos utilizando o padrão do django    
    """
    
    def __obterInstancia(self, email, nome, telefone):
        
        usuario = self.model(
           email = self.normalize_email(email),
           nome = nome,
           telefone = telefone 
        )
        
        return usuario
    
    def create_user(self, email, nome, telefone, password = None):
        """
        Cria um usuário novo
        """
        if not email:
            raise ValueError("O campo email é obrigatório")
        
        usuario = self.__obterInstancia(email, nome, telefone)
        usuario.set_password(password)
        usuario.save(using=self._db)
        
        return usuario
    
    def create_superuser(self, email, nome, telefone, password):
        """
        Cria um novo superuser
        """
        
        usuario = self.__obterInstancia(email, nome, telefone)
        
        usuario.is_admin = True
        usuario.is_active = True
        usuario.set_password(password)
        
        usuario.save(using=self._db)
        
        return usuario

#coding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime

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
    
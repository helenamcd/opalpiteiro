#coding:utf-8
from django.views.generic.edit import FormView

from usuarios.forms import FormCriarUsuario

# Create your views here.
class CadastroUsuario(FormView):
    """
    View baseada em Form para cadastro de usuário
    """
    form_class = FormCriarUsuario
    template_name = 'usuarios/cadastro.html'
    success_url = '/sucesso/'
    
    def form_valid(self, form):
        
        form.save()
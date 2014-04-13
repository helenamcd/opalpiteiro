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
    success_url = '/cadastro/sucesso/'
    
    def form_valid(self, form):
        
        try:
            form.save()
            return super(CadastroUsuario, self).form_valid(form)
        except:
            return self.form_invalid(form)
           

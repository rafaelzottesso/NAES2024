from django.views.generic import TemplateView
from cadastros.models import Pessoa, Cidade
from django.contrib import messages


# Criar uma view para a página inicial
# com herança para a classe TemplateView
class IndexView(TemplateView):
    template_name = "paginas/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Página Inicial"
        context['qtde_pessoas'] = Pessoa.objects.all().count()
        
        if(self.request.user.is_authenticated):
            context['m_pessoas'] = Pessoa.objects.filter(
                cadastrado_por=self.request.user).count()
            
            if(context['m_pessoas'] < 100):
                messages.info(self.request, "Aqui vai uma mensagem")
                messages.success(self.request, "Aqui vai uma mensagem")
                messages.warning(self.request, "Aqui vai uma mensagem")
                messages.error(self.request, "Aqui vai uma mensagem")
            
        context['cidades'] = Cidade.objects.all().order_by('nome')
        context['pessoa'] = Pessoa.objects.get(pk=1)
                    
        return context
    
    
class SobreView(TemplateView):
    template_name = "paginas/sobre.html"
    
from django.views.generic import TemplateView

# Criar uma view para a página inicial
# com herança para a classe TemplateView
class IndexView(TemplateView):
    template_name = "paginas/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Página Inicial"
        return context
    
    
class SobreView(TemplateView):
    template_name = "paginas/sobre.html"
    
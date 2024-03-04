from django.views.generic import TemplateView

# Criar uma view para a página inicial
# com herança para a classe TemplateView
class IndexView(TemplateView):
    template_name = "paginas/index.html"
    
    
class SobreView(TemplateView):
    template_name = "paginas/sobre.html"
    
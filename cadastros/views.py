from .models import Cidade, Pessoa

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import DeleteView

from django.urls import reverse_lazy


class CidadeCreate(CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index') 
    model = Cidade
    fields = ['nome', 'estado']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar cidade'
        return dados
        


class CidadeUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    model = Cidade
    fields = ['nome', 'estado']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar registro de Cidade'
        return dados


##############################################################


class PessoaCreate(CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    model = Pessoa
    fields = [
        'nome_completo', 'nascimento', 'cpf', 'email',
        'rede_social', 'salario', 'cidade',
    ]

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar nova Pessoa'
        return dados
    

class PessoaUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    model = Pessoa
    fields = [
        'nome_completo', 'nascimento', 'cpf', 'email',
        'rede_social', 'salario', 'cidade',
    ]

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de {self.object.nome_completo}"
        return dados
from .models import Cidade, Pessoa

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.urls import reverse_lazy


class CidadeCreate(CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade') 
    model = Cidade
    fields = ['nome', 'estado']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar cidade'
        return dados
        

class CidadeUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')
    model = Cidade
    fields = ['nome', 'estado']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar registro de Cidade'
        return dados


class CidadadeDelete(DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cidade')
    model = Cidade


class CidadeList(ListView):
    template_name = 'cadastros/list/cidade.html'
    model = Cidade


##############################################################


class PessoaCreate(CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoa')
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
    success_url = reverse_lazy('listar-pessoa')
    model = Pessoa
    fields = [
        'nome_completo', 'nascimento', 'cpf', 'email',
        'rede_social', 'salario', 'cidade',
    ]

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de {self.object.nome_completo}"
        return dados
    
    
class PessoaDelete(DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-pessoa')
    model = Pessoa
    
    
class PessoaList(ListView):
    template_name = 'cadastros/list/pessoa.html'
    model = Pessoa
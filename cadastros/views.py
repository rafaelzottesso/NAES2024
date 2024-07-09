from .models import Cidade, Pessoa

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import DeleteView

from django.urls import reverse_lazy


class CidadeCreate(CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    model = Cidade
    fields = ['nome', 'estado']


class CidadeUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    model = Cidade
    fields = ['nome', 'estado']

##############################################################


class PessoaCreate(CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    model = Pessoa
    fields=[
        'nome_completo', 'nascimento', 'cpf', 'email',
        'rede_social', 'salario', 'cidade',
    ]
    

class PessoaUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    model = Pessoa
    fields = [
        'nome_completo', 'nascimento', 'cpf', 'email',
        'rede_social', 'salario', 'cidade',
    ]

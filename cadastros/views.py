from typing import Any
from django.db.models.query import QuerySet
from .models import Cidade, Pessoa

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

# Para usar nas classes
from django.contrib.messages.views import SuccessMessageMixin


class CidadeCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade') 
    model = Cidade
    fields = ['nome', 'estado']
    success_message = "Cidade %(nome)s adicionada com sucesso!"

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar cidade'
        return dados
        

class CidadeUpdate(LoginRequiredMixin, SuccessMessageMixin,  UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')
    model = Cidade
    fields = ['nome', 'estado']
    success_message = "Cidade %(nome)s atualizada!"

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar registro de Cidade'
        return dados


class CidadadeDelete(GroupRequiredMixin, SuccessMessageMixin,  DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cidade')
    model = Cidade
    group_required = ["Administrador"]
    success_message = "Cidade excluída!"

class CidadeList(LoginRequiredMixin, ListView):
    template_name = 'cadastros/list/cidade.html'
    model = Cidade


##############################################################


class PessoaCreate(LoginRequiredMixin, CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoa')
    model = Pessoa
    fields = [
        'nome_completo', 'nascimento', 'cpf', 'email',
        'rede_social', 'salario', 'cidade',
    ]
    
    def form_valid(self, form):
        # Antes de criar objeto e salvar no banco
        form.instance.cadastrado_por = self.request.user
        
        url_sucesso = super().form_valid(form)
        # Depois de criar objeto e salvar no banco
        
        # self.object.nome_completo = self.object.nome_completo + "@"
        # from hashlib import md5
        # self.object.codigo = md5(self.object.pk)
        
        # self.object.save()
        
        return url_sucesso

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar nova Pessoa'
        return dados
    

class PessoaUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoa')
    model = Pessoa
    fields = [
        'nome_completo', 'nascimento', 'cpf', 'email',
        'rede_social', 'salario', 'cidade',
    ]
    
    # Alterar a consulta padrão que retorna o objeto com base no id
    def get_object(self):
        pessoa = Pessoa.objects.get(
            pk=self.kwargs["pk"], 
            # Além do id, faz um WHERE também com o usuário
            cadastrado_por=self.request.user 
        )
        return pessoa

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de {self.object.nome_completo}"
        return dados
    
    
class PessoaDelete(GroupRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-pessoa')
    model = Pessoa
    group_required =["Administrador"]
    
    
class PessoaList(LoginRequiredMixin, ListView):
    template_name = 'cadastros/list/pessoa.html'
    model = Pessoa
    
    # Altera a query padrão para consuultar registros (SELECT)
    def get_queryset(self):
        query = Pessoa.objects.filter(cadastrado_por=self.request.user)
        query = query.select_related("cidade")
        
        return query
    
    # Quanto a queryset é padrão e não é implementada, faça:
    # def get_queryset(self):
    #     return super().get_queryset().select_related("cidade")
    
    
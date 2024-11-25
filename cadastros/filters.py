from django_filters import FilterSet
from .models import Pessoa


class PessoaFilter(FilterSet):
    class Meta:
        model = Pessoa
        fields = {
            'nome_completo' : ['icontains'],
            'nascimento' : ['exact', 'gt', 'lt'],
            'salario' : ['gte', 'lte'],
            'cidade__nome' : ['icontains'],
            'cadastrado_em' : ['year__exact'],
        }


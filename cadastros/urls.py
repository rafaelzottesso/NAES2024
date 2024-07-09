from django.urls import path
# Importe suas views
from .views import CidadeCreate, CidadeUpdate
from .views import PessoaCreate, PessoaUpdate

urlpatterns = [
    # Crie suas urls para as views
    path('cadastrar/cidade/', CidadeCreate.as_view(), name='cadastrar-cidade'),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),
    
    path('cadastrar/pessoa/', PessoaCreate.as_view(), name='cadastrar-pessoa'),
    path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name='editar-pessoa'),
]

from django.contrib import admin

# Importe duas classes
from .models import Cidade, Pessoa

# Register your models here.
admin.site.register(Cidade)
admin.site.register(Pessoa)
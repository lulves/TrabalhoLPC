from django.db import models
from django.contrib.auth.models import User

# Create your models here.  

class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    email = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class PessoaFisica (Pessoa):
    cpf = models.CharField(max_length=11)  

class PessoaJuridica (Pessoa):
    cnpj = models.CharField(max_length=20)
    razaoSocial = models.CharField(max_length=200)

class Autor (Pessoa)
	curriculo = models.CharField(blank=True, null=True)
	artigos = models.CharField(max_length=50, null= True, blank=False)
	
class Evento (models.Model):
    nome = models.CharField(max_length=150)
    eventoPrincipal = models.CharField()
    sigla = models.CharField (max_length=10)
    dataEHoraDeInicio = models.DateField(blank=True, null=True)
    palavraChave =models.CharField(null= True, blank=False)
    logotipo = models.CharField(max_length=50, null= True, blank=False)
    realizador = models.ForeignKey(Pessoa, null= True, blank=False)
    cidade=models.CharField(null= True, blank=False)
    uf =models.CharField(null= True, blank=False)
    endereco =models.CharField(null= True, blank=False)
    cep =models.CharField(null= True, blank=False)

class EventoCientifico (models.Model):
	issn = models.CharField(null= True, blank=False)

class ArtigoCientifico(models.Model):
	titulo = models.CharField(null= True, blank=False)
	autores = models.ForeignKey(Autor, null= True, blank=False)
	evento = models.ForeignKey (EventoCientifico, null= True, blank=False)


from django.db import models

class Doacao(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cidade_bairro = models.CharField(max_length=200)
    itens = models.TextField()
    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField(max_length=550)

    def __str__(self):
        return self.nome

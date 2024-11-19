from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200)  # Nome do produto, limitado a 200 caracteres
    descricao = models.TextField()          # Descrição detalhada do produto
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # Valor com até 10 dígitos e 2 casas decimais
    data_criacao = models.DateTimeField(auto_now_add=True)        # Preenche automaticamente na criação
    data_modificacao = models.DateTimeField(auto_now=True)        # Atualiza sempre que modificado

    def __str__(self):
        return self.nome
        
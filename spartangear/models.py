from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    desconto_percentual = models.DecimalField(max_digits=5, decimal_places=2, help_text="Desconto percentual")
    descricao = models.TextField(null=False, blank=False)
    quantidade = models.PositiveIntegerField()
    variacao_cor = models.ManyToManyField('VariacaoCor')
    variacao_tamanho = models.ManyToManyField('VariacaoTamanho')
    categoria = models.ManyToManyField('Categoria')
    fotos = models.ImageField(upload_to='fotos_produtos/', blank=False, null=True)

    def preco_com_desconto(self):
        preco = self.preco
        if self.desconto_percentual:
            preco *= (1 - self.desconto_percentual / 100)
        return preco

    def __str__(self):
        return self.nome
    
class VariacaoCor(models.Model):
    cor = models.CharField(max_length=10)

    def __str__(self):
        return self.cor

class VariacaoTamanho(models.Model):
    tamanho = models.CharField(max_length=10)

    def __str__(self):
        return self.tamanho

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
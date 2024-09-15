from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False, verbose_name='Nome')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    desconto_percentual = models.DecimalField(max_digits=4, decimal_places=2, help_text="Desconto percentual", verbose_name='Desconto (%)', blank=True)
    descricao = models.TextField(null=False, blank=False, verbose_name='Descrição')
    quantidade = models.PositiveIntegerField(verbose_name='Quantidade em Estoque')
    variacao_cor = models.ManyToManyField('VariacaoCor', related_name='produtos_cor', verbose_name='Variações de Cor')
    variacao_tamanho = models.ManyToManyField('VariacaoTamanho', related_name='produtos_tamanho', verbose_name='Variações de Tamanho')
    categoria = models.ManyToManyField('Categoria', related_name='produtos', verbose_name='Categorias')
    fotos = models.ImageField(upload_to='fotos_produtos/', blank=True, verbose_name='Fotos')

    def preco_com_desconto(self):
        preco = self.preco
        if self.desconto_percentual and 0 <= self.desconto_percentual <= 100:
            preco *= (1 - self.desconto_percentual / 100)
        return preco

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


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
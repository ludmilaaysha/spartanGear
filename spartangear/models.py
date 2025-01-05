from django.db import models
import locale, random
from django.contrib.auth.models import User


# Definir o locale para o Brasil (ou outro local que use vírgula como separador decimal)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Categoria(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.nome

class Cor(models.Model):
    nome = models.CharField(max_length=50)
    codigo_cor = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome

class Tamanho(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Esporte(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Foto(models.Model):
    produto = models.ForeignKey('Produto', related_name='fotos', on_delete=models.CASCADE,)
    imagem = models.ImageField(upload_to="produtos/%Y/%m/%d",)
    
    def __str__(self):
        return f'Foto de {self.produto.nome}'
    
def gerar_id_unico():
    return str(random.randint(100000, 999999))

class Produto(models.Model):
    ref = models.CharField(max_length=6, unique=True, default=gerar_id_unico, editable=False)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    quantidade_estoque = models.PositiveIntegerField()
    cores = models.ManyToManyField(Cor, related_name='produtos', blank=True)
    tamanhos = models.ManyToManyField(Tamanho, related_name='produtos', blank=True)
    esportes = models.ManyToManyField(Esporte, related_name='produtos', blank=False)
    categorias = models.ManyToManyField(Categoria, related_name='produtos')
    destaque = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome

    def preco_com_desconto(self):
        if self.desconto:
            return locale.format_string("%.2f", self.preco - (self.preco * (self.desconto / 100)))
        return locale.format_string("%.2f", self.preco)
    
class Carrinho(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    itens = models.ManyToManyField('ItemCarrinho', related_name='carrinhos')

class ItemCarrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    

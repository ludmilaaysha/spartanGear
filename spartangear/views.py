from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'spartangear/index.html')

def login(request):
    return render(request, 'spartangear/login.html')

def cadastro(request):
    return render(request, 'spartangear/cadastro.html')

def recuperarsenha(request):
    return render(request, 'spartangear/recuperarsenha.html')

def catalogo(request):
    return render(request, 'spartangear/catalogo.html')

def produto(request):
    return render(request, 'spartangear/paginaproduto.html')

def carrinho(request):
    return render(request, 'spartangear/carrinho.html')

def entrega(request):
    return render(request, 'spartangear/entrega.html')

def pagamento(request):
    return render(request, 'spartangear/pagamento.html')

def meucadastro(request):
    return render(request, 'spartangear/meucadastro.html')

def meuspedidos(request):
    return render(request, 'spartangear/meuspedidos.html')

def pedido(request):
    return render(request, 'spartangear/paginapedido.html')

def alterarsenha(request):
    return render(request, 'spartangear/alterarsenha.html')

def ajudaeatendimento(request):
    return render(request, 'spartangear/ajudaeatendimento.html')

def sequenciacompras(request):
    return render(request, 'spartangear/sequencia_compras_fixo.html')
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    dados_produto = {
        1: {"nome": "Tênis Gamma Force Nike Feminino", 
            "preco": 600.00},
            
        2: {"nome": "Tênis Puma Carina Feminino", 
            "preco": 300.00},
    }
    
    return render(request, 'spartangear/index.html', {"produtos": dados_produto})

def login(request):
    return render(request, 'spartangear/login.html')

def cadastro(request):
    return render(request, 'spartangear/cadastro.html')

def recuperarsenha(request):
    return render(request, 'spartangear/recuperarsenha.html')

def catalogo(request):
    dados_produto = {
        1: {"nome": "Tênis Gamma Force Nike Feminino", 
            "preco": 600.00},
            
        2: {"nome": "Tênis Puma Carina Feminino", 
            "preco": 300.00}
    }


    return render(request, 'spartangear/catalogo.html', {"produtos": dados_produto})

def produto(request):
    return render(request, 'spartangear/paginaproduto.html')

def carrinho(request):
    return render(request, 'spartangear/carrinho.html')

@login_required
def entrega(request):
    if request.user.is_authenticated:
        return render(request, 'spartangear/entrega.html')
    else:
        messages.warning(request, "Realize o login para finalizar sua compra")

@login_required
def pagamento(request):
    if request.user.is_authenticated:
        return render(request, 'spartangear/pagamento.html')
    else:
        messages.warning(request, "Realize o login para realizar pagamento")

@login_required
def meucadastro(request):
    if request.user.is_authenticated:
        return render(request, 'spartangear/meucadastro.html')
    else:
        messages.warning(request, "Realize o login para acessar seus dados")

@login_required
def meuspedidos(request):
    if request.user.is_authenticated:
        return render(request, 'spartangear/meuspedidos.html')
    else:
        messages.warning(request, "Realize o login para visualizar seus pedidos")

@login_required
def pedido(request):
    if request.user.is_authenticated:
        # O usuário está autenticado
        return render(request, 'spartangear/paginapedido.html')
    else:
        messages.warning(request, "Realize o login para visualizar o pedido")
    
@login_required
def alterarsenha(request):
    if request.user.is_authenticated:
        # O usuário está autenticado
        return render(request, 'spartangear/alterarsenha.html')
    else:
        messages.warning(request, "Realize o login para alterar a senha")

def ajudaeatendimento(request):
    return render(request, 'spartangear/ajudaeatendimento.html')

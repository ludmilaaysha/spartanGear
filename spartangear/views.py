from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from users.forms import EditCadastroForm, EditarPerfilUsuarioForm
from users.models import PerfilUsuario
from spartangear.models import Carrinho, Cor, ItemCarrinho, Produto, Tamanho
from django.db.models import Q


def index(request):
    produtos = Produto.objects.all()
    return render(request, 'spartangear/index.html', {"cards": produtos})

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

def ajudaeatendimento(request):
    return render(request, 'spartangear/ajudaeatendimento.html')

# def catalogo(request):
#     produtos = Produto.objects.all()
#     return render(request, 'spartangear/catalogo.html', {"cards": produtos})

def catalogo(request):
    produtos = Produto.objects.all()
    nome_a_buscar = request.GET.get('buscar')

    print(f"Nome a buscar: '{nome_a_buscar}'")
    
    if nome_a_buscar:
        # Aplica filtros usando Q objects para busca em múltiplos campos
        try:
            nome_a_buscar_num = int(nome_a_buscar)
            produtos = produtos.filter(
                Q(nome__icontains=nome_a_buscar) |
                Q(categorias__nome__icontains=nome_a_buscar) |
                Q(cores__nome__icontains=nome_a_buscar) |
                Q(ref=nome_a_buscar_num) |  # Se ref é um campo numérico
                Q(esportes__nome__icontains=nome_a_buscar)
            ).distinct()
        except ValueError:
            # Caso a conversão falhe, buscar como texto
            produtos = produtos.filter(
                Q(nome__icontains=nome_a_buscar) |
                Q(categorias__nome__icontains=nome_a_buscar) |
                Q(cores__nome__icontains=nome_a_buscar) |
                Q(ref__icontains=nome_a_buscar) |  # Caso ref seja texto, mesmo se for numérico
                Q(esportes__nome__icontains=nome_a_buscar)
            ).distinct()
    return render(request, 'spartangear/catalogo.html', {'cards': produtos})

def produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    cores = produto.cores.all()
    tamanhos = produto.tamanhos.all()
    return render(request, 'spartangear/paginaproduto.html', {'produto': produto, 'cores': cores, 'tamanhos': tamanhos,})

def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    quantidade = int(request.POST.get('quantidade', 1))
    
    if quantidade > produto.quantidade_estoque:
        messages.error(request, "Quantidade solicitada excede o estoque disponível.")
        return redirect('produto_detalhes', produto_id=produto_id)

    # Adicionar ao carrinho
    item_carrinho, created = ItemCarrinho.objects.get_or_create(produto=produto, quantidade=quantidade)
    carrinho = get_object_or_404(Carrinho, usuario=request.user)
    carrinho.itens.add(item_carrinho)

    messages.success(request, "Produto adicionado ao carrinho.")
    return redirect('carrinho')

def paginapedido(request):
    return render(request, 'spartangear/paginapedido.html')
from django.urls import path
from spartangear import views
from spartangear.views import  adicionar_ao_carrinho, catalogo,  index, produto, carrinho, entrega, pagamento, meuspedidos, pedido, ajudaeatendimento
from users.views import meucadastro
urlpatterns = [
    path('', views.index, name='index'),
    # path('login', login, name='login'),
    # path('cadastro', cadastro, name='cadastro'),
    path('catalogo', catalogo, name='catalogo'),
    path('produto/<int:id>/', produto, name='produto'),
    path('carrinho', carrinho, name='carrinho'),
    path('entrega', entrega, name='entrega'),
    path('pagamento', pagamento, name='pagamento'),
    path('meucadastro', meucadastro, name='meucadastro'),
    path('meuspedidos', meuspedidos, name='meuspedidos'),
    path('pedido', pedido, name='pedido'),
    # path('alterarsenha', alterarsenha, name='alterarsenha'),
    path('ajudaeatendimento', ajudaeatendimento, name='ajudaeatendimento'),
    path('adicionar-ao-carrinho/<int:produto_id>/', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    # path('buscar', buscar, name='buscar',)


]
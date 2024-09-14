from django.urls import path
from spartangear import views
from spartangear.views import index, login, cadastro, recuperarsenha, catalogo, produto, carrinho, entrega, pagamento, meucadastro, meuspedidos, pedido, alterarsenha, ajudaeatendimento
urlpatterns = [
    path('', views.index, name='index'),
    # path('login', login, name='login'),
    # path('cadastro', cadastro, name='cadastro'),
    path('recuperarsenha', recuperarsenha, name='recuperarsenha'),
    path('catalogo', catalogo, name='catalogo'),
    path('produto', produto, name='produto'),
    path('carrinho', carrinho, name='carrinho'),
    path('entrega', entrega, name='entrega'),
    path('pagamento', pagamento, name='pagamento'),
    path('meucadastro', meucadastro, name='meucadastro'),
    path('meuspedidos', meuspedidos, name='meuspedidos'),
    path('pedido', pedido, name='pedido'),
    path('alterarsenha', alterarsenha, name='alterarsenha'),
    path('ajudaeatendimento', ajudaeatendimento, name='ajudaeatendimento'),






]
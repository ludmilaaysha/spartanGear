from django.urls import path

from . import views
from users.views import login, cadastro, logout, alterarsenha, meucadastro, recuperarsenha

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.logout, name='logout'),
    path('meucadastro/', views.meucadastro, name='meucadastro'),
    path('alterarsenha/', views.alterarsenha, name='alterarsenha'),
    path('email_recsenha/', views.email_recsenha, name='email_recsenha'),
    path('recuperarsenha/<str:username>/<str:sessao_token>', views.recuperarsenha, name='recuperarsenha'),

]

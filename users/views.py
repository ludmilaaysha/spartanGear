from django.shortcuts import render 

from users.forms import CadastroForms, LoginForms

def login(request):
    form = LoginForms()
    return render(request, "users/login.html",)

def cadastro(request):
    form = CadastroForms()
    return render(request, "users/cadastro.html",)

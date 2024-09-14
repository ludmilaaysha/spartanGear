from django.shortcuts import render, redirect
from users.forms import CadastroForms, LoginForms
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required


# from users.models import CustomUser

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email_login')
            senha = form.cleaned_data.get('senha')

            usuario = auth.authenticate(
                request,
                username=email,
                password=senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f"{email} logado com sucesso!")
                return redirect('index')
            else:
                messages.warning(request, "Erro ao efetuar login.")
                return redirect('login')

    return render(request, "users/login.html", {"form": form})



# Certifique-se de que o formulário esteja definido corretamente

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():
            senha = form.cleaned_data.get('senha')
            confirmar_senha = form.cleaned_data.get('confirmar_senha')

            if senha != confirmar_senha:
                messages.warning(request, "As senhas não são iguais. Tente novamente.")
                return render(request, 'users/cadastro.html', {'form': form})

            nome = form.cleaned_data.get('nome_cadastro')
            sobrenome = form.cleaned_data.get('sobrenome_cadastro')
            email = form.cleaned_data.get('email_cadastro')

            if User.objects.filter(email=email).exists():
                messages.warning(request, "Usuário já existente")
                return render(request, 'users/cadastro.html', {'form': form})

            # Criação do usuário
            usuario = User.objects.create_user(
                username=email,
                email=email,
                password=senha
            )

            # Adicionar informações adicionais, se necessário
            usuario.first_name = nome
            usuario.last_name = sobrenome
            usuario.save()

            messages.success(request, "Cadastro efetuado com sucesso! Faça login.")

            return redirect('login')

    else:
        form = CadastroForms()

    return render(request, 'users/cadastro.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.info(request, "Logout efetuado com sucesso")
    return redirect('index')
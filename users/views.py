import datetime
from django.shortcuts import render, redirect
from setup import settings
from users.forms import CadastroForms, LoginForms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib import auth, messages
from .models import PerfilUsuario
from django.urls import reverse_lazy
from django.core.mail import send_mail


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
            perfil = PerfilUsuario.objects.create(user=usuario)
            perfil.save()
    

            messages.success(request, "Cadastro efetuado com sucesso! Faça login.")

            return redirect('login')

    else:
        form = CadastroForms()

    return render(request, 'users/cadastro.html', {'form': form})

@login_required
def logout(request):
    auth.logout(request)
    messages.info(request, "Logout efetuado com sucesso")
    return redirect('index')

def convert_to_iso_date(date_str):
    try:
        # Tenta converter a data do formato DD/MM/AAAA para YYYY-MM-DD
        date_obj = datetime.strptime(date_str, '%d/%m/%Y')
        return date_obj.date().isoformat()  # Converte para o formato YYYY-MM-DD
    except ValueError:
        # Retorna None ou trata o erro conforme necessário
        return 0000-00-00

@login_required
def meucadastro(request):
    user = request.user

    try:
        perfil = PerfilUsuario.objects.get(user=user)
    except PerfilUsuario.DoesNotExist:
        perfil = PerfilUsuario(user=user)
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')  # Certifique-se de que o nome do campo está correto
        data_nascimento = request.POST.get('data_nascimento')
        telefone = request.POST.get('telefone')

        # Atualiza os dados do perfil
        if cpf:
            perfil.cpf = cpf
        if data_nascimento:
                # Verifica se a data já está no formato ISO (yyyy-mm-dd)
            try:
                # Tenta converter a data assumindo que está no formato dd/mm/yyyy
                data_nascimento_iso = datetime.datetime.strptime(data_nascimento, '%d/%m/%Y').strftime('%Y-%m-%d')
            except ValueError:
                # Se der erro, a data já está no formato ISO yyyy-mm-dd
                data_nascimento_iso = data_nascimento

            perfil.data_nascimento = data_nascimento_iso
        else:
            perfil.data_nascimento = perfil.data_nascimento

        if telefone:
            perfil.telefone = telefone
        perfil.save()

        # Atualiza os dados do usuário
        usuario = User.objects.get(username=user.email)
        if nome:
            usuario.first_name = nome
        if sobrenome:
            usuario.last_name = sobrenome
        if email:
            usuario.email = email
            usuario.username = email  # Atualizando o username, se necessário
        usuario.save()

        messages.success(request, "Dados atualizados com sucesso!")
        return redirect('meucadastro')

    data_nascimento_iso = perfil.data_nascimento.strftime('%Y-%m-%d') if perfil.data_nascimento else ''
    return render(request, 'users/meucadastro.html', {'perfil': perfil, 'usuario': user, 'data_nascimento_iso': data_nascimento_iso})




@login_required
def alterarsenha(request):
    if request.method == 'POST':
        old_password = request.POST.get('senha_antiga')
        novasenha = request.POST.get('novasenha')
        confirm_novasenha = request.POST.get('confirm_novasenha')

        if novasenha == confirm_novasenha:
            user = User.objects.get(username=request.user.email)
            user.set_password(novasenha)
            user.save()
            messages.success(request,'Senha alterada com sucesso!')
            update_session_auth_hash(request, user)
            return redirect('alterarsenha')
        else:
            messages.warning(request, 'Dados errados')
            return render(request,'users/alterarsenha.html')

    return render(request,'users/alterarsenha.html')

def email_recsenha(request):
    if request.method == 'POST':
        email = request.POST.get('email_recuperacao')
        if User.objects.filter(email__exact = email).exists():
            token = PasswordResetTokenGenerator()
            user=User.objects.get(email = email)
            sessao_token = token.make_token(user)
            username = user.username
            context = {'username': username, 'token': sessao_token}
            send_mail(
                subject = 'Redefinição de senha',
                message = f'Uma requisição de redefinição de senha foi feita no site Spartan Gear para a conta vinculada a este endereço. Para conseguir uma redefinição de senha, acesse o seguinte link: http://127.0.0.1:8000/recuperarsenha/{username}/{sessao_token}',
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [email,],
            )

            return render(request, 'users/email_recsenha.html', {'mensagem': 'E-mail enviado! Cheque sua caixa de entrada.'})
        
        else:
            return render(request, 'users/email_recsenha.html', {'mensagem': 'E-mail não cadastrado!.'})

    return render(request, 'users/email_recsenha.html')

def recuperarsenha(request, username, sessao_token):
    usuario = User.objects.get(username = username)
    senha = request.POST.get('senha')
    confirmar_senha = request.POST.get('confirmar_senha')
    if request.method == 'POST':
        if senha != confirmar_senha:
            return render(request, 'users/recuperarsenha.html', {'mensagem': 'As senhas não coincidem. Tente novamente.'})
        usuario.set_password(senha)
        usuario.save(force_update=True)
        return redirect('login')

    token = PasswordResetTokenGenerator()
    if token.check_token(usuario, sessao_token):
        return render(request, 'users/recuperarsenha.html')
        

def paginaproduto(request):
    cor = request.POST.get(cor)
    tamanho = request.POST.get(tamanho)

    carrinho = Carrinho.objects.update_or_create(item_carrinho)
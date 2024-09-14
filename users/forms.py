from django import forms

class LoginForms(forms.Form):
    email_login=forms.CharField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": 'caixa-digitavel',
                "placeholder": 'Informe seu Email',
            }
        )
    )

    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": 'caixa-digitavel',
                "placeholder": 'Digite sua senha',
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label="Nome*",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": 'caixa-digitavel',
                "placeholder": 'Ex.: José Ricardo',
            }
        )
    )

    sobrenome_cadastro=forms.CharField(
        label="Sobrenome*",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": 'caixa-digitavel',
                "placeholder": 'Ex.: Oliveira Galdi'
            }
        )

    )
    # aniversario_cadastro=forms.DateField(
    #     label="Data de nascimento*",
    #     required=False,
    #     widget=forms.DateInput(
    #         attrs={
    #             "class": 'caixa-digitavel',
    #             "placeholder": 'DD/MM/AAAA'
    #         }
    #     )
    # )

    # phone_cadastro=forms.CharField(
    #     label="Número de telefone",
    #     required=False,
    #     max_length=11,
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": 'caixa-digitavel',
    #             "placeholder": '(99) 99999-9999'
    #         }
    #     )
    # )

    email_cadastro=forms.EmailField(
        label="E-mail*",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": 'caixa-digitavel',
                "placeholder": 'Ex.: jose@gmail.com'
            }
        )
    )

    senha=forms.CharField(
        label="Senha*",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": 'caixa-digitavel',
                "placeholder": 'Digite sua senha',
                "id": "passwordRegister",
            }
        )
    )

    confirmar_senha=forms.CharField(
        label="Confirmar senha*",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": 'caixa-digitavel',
                "placeholder": 'Digite sua senha novamente',
                "id": "confirmPasswordRegister",

            }
        )
    )

    # genero_cadastro=forms.ChoiceField(
    #     label="Gênero*",
    #     required=False,
    #     choices=[
    #         ('masculino', 'Masculino'),
    #         ('feminino', 'Feminino'),
    #         ('nao_informar', 'Prefiro não informar'),
    #     ],
    #     widget=forms.RadioSelect(
    #         attrs={
    #             "class": 'opcao',
    #         }
    #     )
    # )

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")
        
        if senha != confirmar_senha:
            self.add_error('confirmar_senha', 'As senhas não coincidem.')
        
        return cleaned_data
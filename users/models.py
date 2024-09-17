from django.contrib.auth.models import User
from django.db import models

class PerfilUsuario(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('N', 'Prefiro não informar'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField(max_length=10, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    telefone = models.CharField(max_length=16, blank=True, null=True)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)

    def __str__(self):
        return self.user.username


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, senha=None, **extra_fields):
#         if not email:
#             raise ValueError('O e-mail deve ser fornecido')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(senha)
#         user.save(using=self._db)
#         return user

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     nome = models.TextField()
#     sobrenome = models.CharField(max_length=100)
#     aniversario = models.DateField()
#     telefone = models.CharField(max_length=11)
#     genero = models.CharField(max_length=20, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('N', 'Prefiro não informar')])

    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)

    # objects = BaseUserManager()

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['nome', 'sobrenome', 'aniversario', 'telefone', 'genero']

    # def __str__(self):
    #     return self.email

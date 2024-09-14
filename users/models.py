# from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

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

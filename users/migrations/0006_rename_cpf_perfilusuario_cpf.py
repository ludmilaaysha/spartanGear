# Generated by Django 5.1.1 on 2024-09-16 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_perfilusuario_genero_alter_perfilusuario_telefone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfilusuario',
            old_name='CPF',
            new_name='cpf',
        ),
    ]

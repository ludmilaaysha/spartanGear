# Generated by Django 5.1.1 on 2024-09-16 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilusuario',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('N', 'Prefiro não informar')], default='N', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='perfilusuario',
            name='telefone',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]

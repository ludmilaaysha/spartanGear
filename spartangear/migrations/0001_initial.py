# Generated by Django 5.1.1 on 2024-09-14 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VariacaoCor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='VariacaoTamanho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamanho', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('desconto_percentual', models.DecimalField(decimal_places=2, help_text='Desconto percentual', max_digits=5)),
                ('descricao', models.TextField()),
                ('quantidade', models.PositiveIntegerField()),
                ('fotos', models.ImageField(null=True, upload_to='fotos_produtos/')),
                ('categoria', models.ManyToManyField(to='spartangear.categoria')),
                ('variacao_cor', models.ManyToManyField(to='spartangear.variacaocor')),
                ('variacao_tamanho', models.ManyToManyField(to='spartangear.variacaotamanho')),
            ],
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-17 03:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spartangear', '0005_alter_produto_desconto_percentual_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tamanho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='produto',
            name='variacao_cor',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='variacao_tamanho',
        ),
        migrations.AlterModelOptions(
            name='produto',
            options={},
        ),
        migrations.RemoveField(
            model_name='produto',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='desconto_percentual',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='fotos',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='quantidade',
        ),
        migrations.AddField(
            model_name='produto',
            name='categorias',
            field=models.ManyToManyField(related_name='produtos', to='spartangear.categoria'),
        ),
        migrations.AddField(
            model_name='produto',
            name='desconto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='quantidade_estoque',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='produto',
            name='cores',
            field=models.ManyToManyField(blank=True, related_name='produtos', to='spartangear.cor'),
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='produtos/')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='spartangear.produto')),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='tamanhos',
            field=models.ManyToManyField(blank=True, related_name='produtos', to='spartangear.tamanho'),
        ),
        migrations.DeleteModel(
            name='VariacaoCor',
        ),
        migrations.DeleteModel(
            name='VariacaoTamanho',
        ),
    ]

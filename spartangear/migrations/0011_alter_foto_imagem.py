# Generated by Django 5.1.1 on 2024-09-17 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spartangear', '0010_alter_foto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='imagem',
            field=models.ImageField(upload_to='fotosprodutos/%Y/%m/%d'),
        ),
    ]

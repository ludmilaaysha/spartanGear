# Generated by Django 5.1.1 on 2024-09-17 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spartangear', '0008_cor_codigo_cor'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='destaque',
            field=models.BooleanField(default=False),
        ),
    ]

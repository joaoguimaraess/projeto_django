# Generated by Django 4.2.7 on 2023-11-27 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_padaria', '0003_alter_fila1_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fila1',
            name='name',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
# Generated by Django 4.0.4 on 2023-08-11 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado em '),
        ),
    ]
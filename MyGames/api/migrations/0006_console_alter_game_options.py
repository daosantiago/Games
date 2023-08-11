# Generated by Django 4.2.4 on 2023-08-11 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_game_name_game_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Console',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em ')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado em ')),
                ('active', models.BooleanField()),
                ('name', models.CharField(max_length=250, verbose_name='Nome da consola')),
            ],
            options={
                'verbose_name': 'Console',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['title'], 'verbose_name': 'Jogo'},
        ),
    ]

# Generated by Django 4.0.4 on 2023-08-11 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_console_shortname_game_imagem_alter_console_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em ')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado em ')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('name', models.CharField(max_length=50, verbose_name='Gênero de jogo')),
            ],
            options={
                'verbose_name': 'Gênero',
                'ordering': ['name'],
            },
        ),
    ]
# Generated by Django 4.0.4 on 2023-08-11 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_game_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.genre'),
        ),
    ]

# Generated by Django 4.0.4 on 2023-08-15 16:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0025_alter_evaluation_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='evaluation',
            unique_together={('user', 'platform', 'game')},
        ),
    ]

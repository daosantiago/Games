from django.db import models

# Create your models here.

class Item(models.Model):
    description = models.TextField("Descrição")
    created = models.DateTimeField('Criado em ', auto_now_add=True)
    updated = models.DateTimeField('Atualizado em ', auto_now=True)
    active = models.BooleanField()

    class Meta:
        abstract = True



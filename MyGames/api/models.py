from django.db import models


class Item(models.Model):
    description = models.TextField("Descrição")
    created = models.DateTimeField('Criado em ', auto_now_add=True)
    updated = models.DateTimeField('Atualizado em ', auto_now=True)
    active = models.BooleanField()

    class Meta:
        abstract = True


class Game(Item):
    name = models.CharField("<NAME>", max_length=1024, unique=True)

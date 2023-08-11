from django.db import models

# Create your models here.

class Item(models.Model):
    description = models.TextField("Descrição")
    created = models.DateTimeField('Criado em ', auto_created=True)
    updated = models.DateTimeField('Atualizado em ', auto_now= True)
    

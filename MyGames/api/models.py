from django.db import models


class Item(models.Model):
    """Modelo para representar as informações comuns para todas as tabelas do banco de dados"""
    description = models.TextField("Descrição")
    created = models.DateTimeField('Criado em ', auto_now_add=True)
    updated = models.DateTimeField('Atualizado em ', auto_now=True)
    active = models.BooleanField()

    class Meta:
        abstract = True


class Game(Item):
    """Modelo para representar os jogos cadastrados"""
    title = models.CharField("Nome do jogo", max_length=1024, unique=True)
    # imagem = models.ImageField("Capa do Jogo ", upload_to="games")
    
    class Meta:
        verbose_name='Jogo'
        ordering=['title']

    def __str__(self):
        return self.titulo
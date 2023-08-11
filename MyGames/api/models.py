from django.db import models


class Item(models.Model):
    """Modelo para representar as informações comuns para todas as tabelas do banco de dados"""
    description = models.TextField("Descrição")
    created = models.DateTimeField('Criado em ', auto_now_add=True)
    updated = models.DateTimeField('Atualizado em ', auto_now=True)
    active = models.BooleanField("Ativo", default=True)

    class Meta:
        abstract = True


class Game(Item):
    """Modelo para representar os jogos cadastrados"""
    title = models.CharField("Nome do jogo", max_length=1024, unique=True)
    imagem = models.ImageField("Capa do Jogo ", upload_to="games")
    
    class Meta:
        verbose_name='Jogo'
        ordering=['title']

    def __str__(self):
        return self.title

    
class Console(Item):
    """Modelo para representar o consoles de video game"""
    name = models.CharField("Nome do console",max_length=250)
    shortName = models.CharField("Abreviação ou Apelido", max_length=50)


    class Meta:
        verbose_name='Console'
        ordering=['name']

    def __str__(self):
        return self.name

class Genre(Item):
    name = models.CharField("Gênero de jogo",max_length=50)

    class Meta:
        verbose_name='Gênero'
        ordering=['name']
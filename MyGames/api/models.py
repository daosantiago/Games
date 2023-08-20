from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Item(models.Model):
    """Modelo para representar as informações comuns para todas as tabelas do banco de
    dados"""

    description = models.TextField("Descrição", blank=True, null=True)
    created = models.DateTimeField("Criado em ", auto_now_add=True)
    updated = models.DateTimeField("Atualizado em ", auto_now=True)
    active = models.BooleanField("Ativo", default=True)

    class Meta:
        abstract = True


class Genre(Item):
    name = models.CharField("Gênero de jogo", max_length=50)

    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Difficulty(Item):
    # name = models.CharField("Dificuldade do jogo", max_length=3)
    CHOICES = [
        ("AAA", "AAA - O Mais Difícil"),
        ("AA", "AA - Muito Difícil"),
        ("A", "A - Difícil"),
        ("B", "B - Médio"),
        ("C", "C - Fácil"),
    ]
    difficulty = models.CharField(
        "Nível", max_length=3, choices=CHOICES, unique=True, null=True
    )

    def get_difficulty_name(self):
        # Retorna o nome correspondente à dificuldade selecionada
        for code, difficulty in self.CHOICES:
            if code == self.difficulty:
                return difficulty
        return "Desconhecido"

    # Define o campo de leitura apenas para o nome da dificuldade
    difficulty_name = property(get_difficulty_name)

    # name = models.CharField("Nome", max_length=50, unique=True)
    description = models.TextField("Descrição", blank=True, null=True)

    class Meta:
        verbose_name = "Dificuldade"
        verbose_name_plural = "Dificuldades"
        ordering = ["difficulty"]

    def __str__(self):
        return self.name


class Company(Item):
    """Modelo para represnetar a empresa dona do console."""

    name = models.CharField(
        "Nome da Empresa", max_length=128, unique=True, blank=False, null=False
    )

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Console(Item):
    """Modelo para representar o consoles de video game"""

    name = models.CharField("Nome do console", max_length=250)
    shortName = models.CharField("Abreviação ou Apelido", max_length=50, blank=True)
    generation = models.CharField(
        "Geração do console", max_length=250, blank=True, null=True
    )
    color = models.CharField("Cor do console", blank=True, max_length=15)
    company = models.ForeignKey(
        Company,
        verbose_name="Empresa",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Console"
        verbose_name_plural = "Consoles"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Game(Item):
    """Modelo para representar os jogos cadastrados"""

    title = models.CharField("Nome do jogo", max_length=1024)
    imagem = models.ImageField("Capa do Jogo ", upload_to="games", blank=True)
    genre = models.ForeignKey(
        Genre, verbose_name="Gênero", on_delete=models.CASCADE, blank=True, null=True
    )
    platform = models.ForeignKey(
        Console,
        verbose_name="Plataforma",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Jogo"
        verbose_name_plural = "Jogos"
        ordering = ["title"]
        unique_together = [
            [
                "title",
                "platform",
            ]
        ]

    def __str__(self):
        return self.title


class Evaluation(Item):
    """Modelo para representar avaliação dos usuários"""

    user = models.ForeignKey(User, verbose_name="Usuário", on_delete=models.CASCADE)
    title = models.CharField(
        "Título da avaliação", max_length=50, blank=True, null=True
    )
    platform = models.ForeignKey(
        Console,
        verbose_name="Plataforma",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    game = models.ForeignKey(
        Game,
        verbose_name="Jogo",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    score = models.IntegerField(
        "Nota",
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )

    game_time = models.DurationField("Tempo de jogo", blank=True, null=True)
    # instance = MyModel.objects.create(duration=timedelta(days=2))

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        ordering = ["updated"]
        unique_together = [["user", "platform", "game"]]

    def __str__(self):
        return self.title

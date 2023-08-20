from django.contrib import admin

from .forms import EvaluationForm

from .models import Game, Console, Genre, Difficulty, Evaluation, Company

# Register your models here.


class Games(admin.ModelAdmin):
    list_display = (
        "id",
        "platform",
        "title",
        "genre",
        "description",
        "created",
        "updated",
    )
    list_display_links = ("id", "title")

    fieldsets = (
        (
            "Informações do jogo",
            {
                "fields": ["title", "imagem", "genre", "platform"],
            },
        ),
        ("Descrição", {"fields": ["description"]}),
    )

    search_fields = ("title",)
    list_per_page = 20

    class Meta:
        model = Game


class Consoles(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "shortName",
        "company",
        "description",
        "created",
        "updated",
    )
    list_display_links = ("id", "name", "shortName")

    fields = ("name", "shortName", "company", "generation", "color", "description")
    search_fields = ("name",)
    list_per_page = 20

    class Meta:
        model = Console


class Genres(admin.ModelAdmin):
    list_display = ("id", "name", "description", "created", "updated")
    list_display_links = ("id", "name")

    fields = ("name", "description")
    search_fields = ("name",)
    list_per_page = 20

    class Meta:
        model = Genre


class Companies(admin.ModelAdmin):
    list_display = ("id", "name", "description", "created", "updated")
    list_display_links = ("id", "name")

    fields = ("name", "description")
    search_fields = ("name",)
    list_per_page = 20

    class Meta:
        model = Company


class Evaluations(admin.ModelAdmin):
    list_display = ("id", "title", "user")
    list_display_links = ("id", "title")
    readonly_fields = ("user",)

    fields = ("title", "description", "platform", "game", "user")

    class Meta:
        model = Evaluation

    # def save_form(self, request, form, change):
    #     obj = super(Evaluations, self).save_form(request, form, change)
    #     if not change:
    #         obj.user = request.user
    #     return obj

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


class DifficultyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "difficulty",
        "difficulty_name",
        "description",
        "created",
        "updated",
    )


class EvaluationAdmin(admin.ModelAdmin):
    form = EvaluationForm
    list_display = ("id", "title", "user")
    list_filter = ("platform",)
    add_form_template = "cad_evaluation.html"
    change_form_template = "cad_evaluation.html"
    # fields = ("title", "description", "platform", "game", "user")

    fieldsets = (
        (
            "Informações do jogo",
            {
                "fields": ["title", "platform", "game", "score", "user"],
            },
        ),
        (
            "Texto",
            {
                "fields": [
                    "description",
                ]
            },
        ),
    )

    readonly_fields = ("user",)


admin.site.register(Game, Games)
admin.site.register(Console, Consoles)
admin.site.register(Genre, Genres)
# admin.site.register(Evaluation, Evaluations)
admin.site.register(Evaluation, EvaluationAdmin)
admin.site.register(Company, Companies)
admin.site.register(Difficulty, DifficultyAdmin)

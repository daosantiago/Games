from django.contrib import admin

from .models import Game, Console, Genre, Difficulty, Evaluation

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
    list_display = ("id", "name", "description", "created", "updated")
    list_display_links = ("id", "name")

    fields = ("name", "shortName", "description")
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


admin.site.register(Game, Games)
admin.site.register(Console, Consoles)
admin.site.register(Genre, Genres)
admin.site.register(Evaluation, Evaluations)

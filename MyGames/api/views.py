from django.shortcuts import render
from .models import Game


# Create your views here.
def myEvaluationView(request):
    id = request.GET.get("id_platform")
    games = Game.objects.filter(platform_id=id)
    return render(request, "get_game.html", {"games": games})

from django.urls import path
from . import views

urlpatterns = [
    path("ajax/get-games/", views.myEvaluationView, name="ajax_get_games"),
]

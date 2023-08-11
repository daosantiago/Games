from django.contrib import admin

from .models import Game

# Register your models here.


class Games(admin.ModelAdmin):
  list_display = ('name', 'description')
  class Meta:
    model=Game
    admin.site.register([Game])
    
from django.contrib import admin

from .models import Game, Console

# Register your models here.


class Games(admin.ModelAdmin):
  list_display = ('id', 'title', 'description', 'created', 'updated')
  list_display_links = ('id', 'title')
  search_fields = ('title',)
  list_per_page = 20

  class Meta:
    model=Game

admin.site.register(Game, Games)
    
class Consoles(admin.ModelAdmin):
  list_display = ('id', 'name', 'description', 'created', 'updated')
  list_display_links = ('id', 'name')
  search_fields = ('name',)
  list_per_page = 20
  
  class Meta:
    model=Game

admin.site.register(Console, Consoles)
    
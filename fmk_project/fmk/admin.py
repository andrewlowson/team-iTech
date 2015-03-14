from django.contrib import admin
from fmk.models import Player, Category, Celebrity, Game, Result

class CategoryAdmin (admin.ModelAdmin):
    list_display = ('name', 'description')

class CelebrityAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'category',
        str('fuck_count'),
        str('marry_count'),
        str('kill_count'),
        'picture',
    )

class GameAdmin (admin.ModelAdmin):
    list_display = (
        'celebrity1',
        'celebrity2',
        'celebrity3',
    )

class ResultAdmin (admin.ModelAdmin):
    list_display = (
        'game_name',
        'player',
        'result1',
        'result2',
        'result3',
    )

# Register your models here.
admin.site.register(Player)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Celebrity, CelebrityAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Result, ResultAdmin)
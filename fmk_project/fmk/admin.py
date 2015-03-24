from django.contrib import admin
from fmk.models import Player, Category, Celebrity, Game, Result

# The fields to be displayed in the Category page of admin
class CategoryAdmin (admin.ModelAdmin):
    list_display = ('name', 'description')

# The fields to be displayed in the Player page of admin
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        str('gamesPlayed'),
    )

# The fields to be displayed in the Celebrity page of admin
class CelebrityAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'category',
        str('fuck_count'),
        str('marry_count'),
        str('kill_count'),
        str('num_results'),
        'picture',
    )

# The fields to be displayed in the Game page of admin
class GameAdmin (admin.ModelAdmin):
    list_display = (
        'celebrity1',
        'celebrity2',
        'celebrity3',
    )

# The fields to be displayed in the Results page of admin
class ResultAdmin (admin.ModelAdmin):
    list_display = (
        'game_name',
        'player',
        'result1',
        'result2',
        'result3',
    )

# Registeration of the models.
admin.site.register(Player, PlayerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Celebrity, CelebrityAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Result, ResultAdmin)

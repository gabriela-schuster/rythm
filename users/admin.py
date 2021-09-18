from django.contrib import admin
from .models import Level


class LevelAdmin(admin.ModelAdmin):
	list_display = ('xp_total', 'user')


admin.site.register(Level, LevelAdmin)

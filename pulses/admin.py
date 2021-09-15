from django.contrib import admin
from .models import Pulse

class PulseAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'conclusion_time')
	list_per_page = 10


admin.site.register(Pulse)

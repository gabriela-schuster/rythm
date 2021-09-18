from django.contrib import admin
from .models import Pulse


class PulseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',
                    'conclusion_time', 'concluded', 'player')
    list_per_page = 20


admin.site.register(Pulse, PulseAdmin)

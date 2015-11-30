from django.contrib import admin
from .models import Host
from .models import Ping


class PingAdmin(admin.ModelAdmin):
    list_display = ('host', 'timestamp', 'success')


admin.site.register(Host)
admin.site.register(Ping, PingAdmin)

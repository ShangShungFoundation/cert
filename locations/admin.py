from django.contrib import admin

from models import Location


class LocationAdmin(admin.ModelAdmin):
    list_display = ()

admin.site.register(Location, LocationAdmin)


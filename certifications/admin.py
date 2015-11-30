from django.contrib import admin

from models import Certification, Accreditation, Location


class CertificationAdmin(admin.ModelAdmin):
    list_display = ()


class AccreditationAdmin(admin.ModelAdmin):
    list_display = ()


class LocationAdmin(admin.ModelAdmin):
    list_display = ()


admin.site.register(Certification, CertificationAdmin)
admin.site.register(Accreditation, AccreditationAdmin)
admin.site.register(Location, LocationAdmin)

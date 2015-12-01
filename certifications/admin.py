from django.contrib import admin

from authorities.models import Certifier

from models import Certification, Accreditation, Location


class CertificationAdmin(admin.ModelAdmin):
    list_display = ("type", "name", "authority", )
    list_filter = ( "type", )

    fieldsets = (
        (None, {
            'fields': (
                "name",
                "authority",
                "requires",
                "description",
                "file",
            )
        }),
    )

    def save_model(self, request, obj, form, change):
        #import ipdb; ipdb.set_trace()
        if getattr(obj, 'created_by', None) is None:
            obj.created_by_id = request.user.id
        obj.save()



class AccreditationAdmin(admin.ModelAdmin):
    list_display = ("certification", "released_at", "location")
    list_filter = ( "certification", "location")

    fieldsets = (
        (None, {
            'fields': (
                "certification",
                "certifiers",
                "released_at",
                "location",
                "description",
            )
        }),
    )

    def save_model(self, request, obj, form, change):
        #import ipdb; ipdb.set_trace()
        if getattr(obj, 'created_by', None) is None:
            obj.created_by_id = request.user.id
        obj.save()


class LocationAdmin(admin.ModelAdmin):
    list_display = ()


admin.site.register(Certification, CertificationAdmin)
admin.site.register(Accreditation, AccreditationAdmin)
admin.site.register(Location, LocationAdmin)

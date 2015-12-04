from django.contrib import admin

from authorities.models import Certifier

from models import Discipline, Certification
from models import Accreditation, Certificate


class CertificationAdmin(admin.ModelAdmin):
    list_display = ("name","cert_type", "authority", )
    list_filter = ( "cert_type", )

    fieldsets = (
        (None, {
            'fields': (
                "name",
                "title",
                "authority",
                "cert_type",
                "discipline",
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


class Certificateline(admin.TabularInline):
    model = Certificate
    exclude = ['created_by']
    raw_id_fields = ('person',)

    def save_model(self, request, obj, form, change):
        #import ipdb; ipdb.set_trace()
        if getattr(obj, 'created_by', None) is None:
            obj.created_by_id = request.user.id
        obj.save()


class AccreditationAdmin(admin.ModelAdmin):
    list_display = ("certification", "released_at", "location")
    list_filter = ( "certification", "location")
    inlines = [Certificateline]

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




class CertificateAdmin(admin.ModelAdmin):
    list_display = ("person", "accreditation")
    list_filter = ( "accreditation", )
    search_fields = ('person__second_name', 'person__email', )
    raw_id_fields = ("person", )

    fieldsets = (
        (None, {
            'fields': (
                "person",
                "accreditation",
                "observations",
            )
        }),
    )

    def save_model(self, request, obj, form, change):
        #import ipdb; ipdb.set_trace()
        if getattr(obj, 'created_by', None) is None:
            obj.created_by_id = request.user.id
        obj.save()

admin.site.register(Discipline)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(Accreditation, AccreditationAdmin)
admin.site.register(Certificate, CertificateAdmin)

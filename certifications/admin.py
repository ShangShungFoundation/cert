from django.contrib import admin

from authorities.models import Certifier

from models import Discipline, CertificationProgramme
from models import Accreditation, Certificate


class CertificationProgrammeAdmin(admin.ModelAdmin):
    list_display = ("name","cert_type", "authority", )
    list_filter = ( "cert_type", )

    fieldsets = (
        (None, {
            'fields': (
                "name",
                "title",
                "cert_type",
                "expiery",
                "discipline",
                "cert_template",
            )
        }),
        ("Authority", {
            'fields': (
                "authority",
                "certifiers",
            )
        }),
        ("requirements", {
            'fields': (
                "requires",
                "prerequisities",
            )
        }),
        ("requirements", {
            'fields': (
                "summary",
                "description",
                "achivement",
            )
        }),
    )

    def save_model(self, request, obj, form, change):
        #import ipdb; ipdb.set_trace()
        if getattr(obj, 'created_by', None) is None:
            obj.created_by_id = request.user.id
        obj.save()


class CertificateInline(admin.TabularInline):
    model = Certificate
    exclude = ['created_by']
    raw_id_fields = ('student',)

    def save_model(self, request, obj, form, change):
        #import ipdb; ipdb.set_trace()
        if getattr(obj, 'created_by', None) is None:
            obj.created_by_id = request.user.id
        obj.save()


class AccreditationAdmin(admin.ModelAdmin):
    list_display = ("certification", "released_at", "location")
    list_filter = ( "certification", "location")
    inlines = [CertificateInline]

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
        if getattr(obj, 'created_by', None) is None:
            obj.created_by_id = request.user.id
        obj.save()


class CertificateAdmin(admin.ModelAdmin):
    #list_display = ("person", "accreditation")
    list_filter = ( "accreditation", )
    search_fields = ('student__second_name', 'student__email', )
    raw_id_fields = ("student", )

    fieldsets = (
        (None, {
            'fields': (
                "student",
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
admin.site.register(CertificationProgramme, CertificationProgrammeAdmin)
admin.site.register(Accreditation, AccreditationAdmin)
admin.site.register(Certificate, CertificateAdmin)

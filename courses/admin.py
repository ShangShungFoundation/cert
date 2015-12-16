from django.contrib import admin


from models import EducationalProgramme, Module
from models import ParticipantGroup, Participant
from models import Course, Fee, ProgrammeResource, Communication


class _CreatedAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_by', None) is None:
            obj.created_by_id = request.user.id
        obj.save()	


class FeeInline(admin.TabularInline):
    model = Fee
    exclude = ['created_by']

    def save_model(self, request, obj, form, change):
        #import ipdb; ipdb.set_trace()
        if getattr(obj, 'created_by', None) is None:
            obj.created_by_id = request.user.id
        obj.save()


class ProgrammeResourceInline(admin.StackedInline):
    model = ProgrammeResource
    exclude = ['created_by']
    extra=1

    def save_model(self, request, obj, form, change):
        #import ipdb; ipdb.set_trace()
        if getattr(obj, 'created_by', None) is None:
            obj.created_by_id = request.user.id
        obj.save()


class ModuleInline(admin.StackedInline):
    model = Module
    exclude = ['created_by']
    extra=1

    def save_model(self, request, obj, form, change):
        #import ipdb; ipdb.set_trace()
        if getattr(obj, 'created_by', None) is None:
            obj.created_by_id = request.user.id
        obj.save()


class EducationalProgrammeAdmin(_CreatedAdmin):
    list_display = ("title", "institution", "is_active")
    list_filter = ( "is_active", "institution")
    inlines = [ModuleInline, FeeInline, ProgrammeResourceInline]

    fieldsets = (
        (None, {
            'fields': (
                "title",
                "institution",
                "is_active",
            )
        }),
        ("description", {
            'fields': (
                "summary",
                "programme",
            )
        }),
        ("requirements", {
            'fields': (
                "requires",
                "public",
            )
        }),
        ("achivement", {
            'fields': (
                "achivement",
                "certification",
            )
        }),
    )


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("person", "course", "payed", "status")
    list_filter = ( "status", "course__title")
    raw_id_fields = ("person", "certificate")
    fieldsets = (
        (None, {
            'fields': (
            	"course",
                ("person", "payed"),
                ("status", "certificate"),
                "observations",
            )
        }),
    )


class ParticipantInline(admin.StackedInline):
    model = Participant
    raw_id_fields = ("person", "certificate")
    extra = 1
    fieldsets = (
        (None, {
            'fields': (
                ("person", "payed"),
                ("status", "certificate"),
                "observations",
            )
        }),
    )


class CourseAdmin(_CreatedAdmin):
    list_display = ("educational_programme", "location", "begins", "status")
    list_filter = ("educational_programme__title", "status", "location__name")
    inlines = [ParticipantInline]

    fieldsets = (
        (None, {
            'fields': (
                "educational_programme",
                "title",
                "accreditation",
                "location",
            )
        }),
        ("organization", {
            'fields': (
                "organizer",
                "manager",
                "professors"
            )
        }),
        ("languages", {
            'fields': (
                "main_language",
                "second_language",
            )
        }),
        ("timeing", {
            'fields': (
                ("begins", "finish"),
                "timetable",
            )
        }),
        ("recrutation", {
            'fields': (
                ("min_nbr_participants", "max_nbr_participants"),
                "recrutation_starts",
            )
        }),
        ("status", {
            'fields': (
            	"status",
                "observations",
            )
        }),
    )

class FeeAdmin(_CreatedAdmin):
    list_display = ("programme", "participant_group", "zone")

    def save_model(self, request, obj, form, change):
        #import ipdb; ipdb.set_trace()
        if getattr(obj, 'created_by', None) is None:
            obj.created_by_id = request.user.id
        obj.save()


class ProgrammeResourceAdmin(_CreatedAdmin):
    list_display = ("course", "file", "type")
    list_filter =  ("type", )
    list_search = ("educational_programme__title", "title")


class CommunicationAdmin(admin.ModelAdmin):
    list_display = ("course", "subject", "sent_at")

    def save_model(self, request, obj, form, change):
        #import ipdb; ipdb.set_trace()
        if getattr(obj, 'sent_by', None) is None:
            obj.sent_by = request.user.id
        obj.save()


admin.site.register(EducationalProgramme, EducationalProgrammeAdmin)
admin.site.register(Module)
admin.site.register(ParticipantGroup)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Fee, FeeAdmin)
admin.site.register(ProgrammeResource, ProgrammeResourceAdmin)
admin.site.register(Communication, CommunicationAdmin)

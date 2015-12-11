from django.contrib import admin


from models import EducationalProgramme
from models import ParticipantGroup, Participant
from models import Course, Fee, File, Communication


class EducationalProgrammeAdmin(admin.ModelAdmin):
    list_display = ("title", "institution")


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("person", "course", "payed", "status")


class CourseAdmin(admin.ModelAdmin):
    list_display = ("educational_programme", "location", "begins", "status")


class FeeAdmin(admin.ModelAdmin):
    list_display = ("programme", "participant_group", "zone")


class FileAdmin(admin.ModelAdmin):
    list_display = ("course", "file", "type")


class CommunicationAdmin(admin.ModelAdmin):
    list_display = ("course", "subject", "sent_at")


admin.site.register(EducationalProgramme, EducationalProgrammeAdmin)
admin.site.register(ParticipantGroup)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Fee, FeeAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Communication, CommunicationAdmin)
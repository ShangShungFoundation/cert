from django.contrib import admin

from models import Course, Participant


class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "begins", "organizer", "status")


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("person", "course", "payed", "status")


admin.site.register(Course, CourseAdmin)
admin.site.register(Participant, ParticipantAdmin)

from django.contrib import admin

from models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "idc_member")
    search_fields = ('first_name', 'last_name', "email")

    fieldsets = (
        (None, {
            'fields': (
                "treatment", 
                ("first_name", "last_name"),
                "birth",
                "idc_member",
            )
        }),
        ('Contact', {
            'fields': (
                "tel",
                ("email", "receives_newsletters"),
            )
        }),
        ('Address', {
            'fields': (
                "address",
                "country",
            )
        }),
    )

    def save_model(self, request, obj, form, change):
        #import ipdb; ipdb.set_trace()
        if getattr(obj, 'created_by', None) is None:
            obj.created_by_id = request.user.id
        obj.save()

admin.site.register(Student, StudentAdmin)


from django.contrib import admin


from models import Person, Certificate


class PersonAdmin(admin.ModelAdmin):
    list_display = ()


class CertificateAdmin(admin.ModelAdmin):
    list_display = ()

admin.site.register(Person, PersonAdmin)
admin.site.register(Certificate, CertificateAdmin)

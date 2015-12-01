from django.contrib import admin

# Register your models here.
from models import Authority, Certifier


class AuthorityAdmin(admin.ModelAdmin):
    list_display = ("name", )


class CertifierAdmin(admin.ModelAdmin):
    list_display = ("person", "role")
    raw_id_fields = ("person", )
    fieldsets = (
        (None, {
            'fields': (
            	"person",
                "role",
            )
        }),
    )

admin.site.register(Authority, AuthorityAdmin)
admin.site.register(Certifier, CertifierAdmin)

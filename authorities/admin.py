from django.contrib import admin

# Register your models here.
from models import Authority, Certifier


class AuthorityAdmin(admin.ModelAdmin):
    list_display = ()


class CertifierAdmin(admin.ModelAdmin):
    list_display = ()

admin.site.register(Authority, AuthorityAdmin)
admin.site.register(Certifier, CertifierAdmin)

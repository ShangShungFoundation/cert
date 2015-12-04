from django.shortcuts import render
from django import forms
from django.core import validators

from models import Certification, Certificate


class CertVerifyForm(forms.Form):
    search = forms.CharField(max_length=100)


def certifications(request):
    certifications = Certification.objects.all()
    return render(request, "certifications/certifications.html",
        dict(certifications=certifications) )

def certification(request, object_id):
    certification = Certification.objects.get(pk=object_id)
    cert_verify_form = CertVerifyForm(request.GET)
    return render(request, "certifications/certification.html",
        dict(certification=certification,
            cert_verify_form=cert_verify_form) )

def certificate(request, email):
    cert = Certificate.objects.get(person__email=email)
    return render(request, "certifications/certificate.html",
        dict(cert=cert) )

def certificates(request, certification_id):
    search_str = request.GET.get("search")
    try:
        is_email = validators.validate_email(search_str)
    except validators.ValidationError:
        certs = Certificate.objects.filter(person__last_name=search_str, )
    else:
        certs = Certificate.objects.filter(person__email=search_str)

    return render(request, "certifications/certificates.html",
        dict(certs=certs, search_str=search_str) )

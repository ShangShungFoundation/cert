from django.shortcuts import render
from django import forms

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

from django.shortcuts import render

from models import Certification, Certificate


def certifications(request):
    certifications = Certification.objects.all() or None
    return render(request, "certifications/certifications.html",
        dict(certifications=certifications) )

def certification(request, object_id):
    certification = Certification.objects.get(pk=object_id)
    return render(request, "certifications/certification.html",
        dict(certification=certification) )

def certificate(request, email):
    cert = Certificate.objects.get(person__email=email)
    return render(request, "certifications/certificate.html",
        dict(cert=cert) )

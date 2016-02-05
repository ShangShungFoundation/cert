from django.shortcuts import render

from models import EducationalProgramme, Course, Fee
from certifications.models import Discipline, CertificationProgramme

def programmes(request):
    programmes = EducationalProgramme.active.all()
    return render(request, "courses/programmes.html",
        dict(programmes=programmes))


def programme(request, object_id):
    programme = EducationalProgramme.active.get(pk=object_id)
    return render(request, "courses/programme.html",
        dict(programme=programme))


def open_courses(request):
    courses = Course.objects.opened()
    return render(request, "courses/open_courses.html",
        dict(courses=courses))


def course(request, object_id):
    course = Course.objects.get(pk=object_id)
    fees = Fee.objects.filter(
        programme_id=course.educational_programme.id,
        zone_id=course.location.zone_id)
    return render(request, "courses/course.html",
        dict(course=course, fees=fees))


def recruit(request, object_id):
    course = Course.active.get(pk=object_id)
    return render(request, "courses/course.html",
        dict(courses=courses))


def discipline(request, object_id):
    discipline = Discipline.objects.get(pk=object_id)
    educational_programmes = EducationalProgramme.active.filter(discipline_id=object_id)
    courses = Course.objects.filter(educational_programme__discipline_id=object_id)
    certification_programmes = CertificationProgramme.objects.filter(discipline_id=object_id)
    return render(request, "courses/discipline.html",
        dict(discipline=discipline, 
            educational_programmes=educational_programmes,
            certification_programmes=certification_programmes))


def _get_opened_courses_for_certification(cert_id):
    try:
        educational_programme = EducationalProgramme.active.get(certification_id = cert_id)
    except EducationalProgramme.DoesNotExist:
        return []
    else:
        courses = Course.objects.opened().filter(educational_programme=educational_programme)
        return courses
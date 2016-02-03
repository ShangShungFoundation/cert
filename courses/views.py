from django.shortcuts import render

from models import EducationalProgramme, Course, Fee


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


def _get_opened_courses_for_certification(cert_id):
    try:
        educational_programme = EducationalProgramme.active.get(certification_id = cert_id)
    except EducationalProgramme.DoesNotExist:
        return []
    else:
        courses = Course.objects.opened().filter(educational_programme=educational_programme)
        return courses
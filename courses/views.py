from django.shortcuts import render

from models import EducationalProgramme, Course


def programmes(request):
    programmes = EducationalProgramme.active.all()
    return render(request, "courses/programmes.html",
        dict(programmes=programmes) )


def programme(request, object_id):
    programme = EducationalProgramme.active.get(pk=object_id)
    return render(request, "courses/programme.html",
        dict(programme=programme) )


def open_courses(request):
    courses = Course.objects.opened()
    return render(request, "courses/open_courses.html",
        dict(courses=courses) )


def course(request, object_id):
    course = Course.objects.get(pk=object_id)
    return render(request, "courses/course.html",
        dict(course=course) )


def recruit(request, object_id):
    course = Course.active.get(pk=object_id)
    return render(request, "courses/course.html",
        dict(courses=courses) )
import datetime 
import pycountry

from django.db import models
from django.contrib.auth.models import User

from locations.models import Location, Zone
from students.models import Student
from certifications.models import CertificationProgramme
from certifications.models import Accreditation, Certificate
from authorities.models import Authority

from certifications.models import Discipline

LANGUAGES = [(c.name, c.name) for c in pycountry.languages]


class ActiveProgrammeManager(models.Manager):
    def get_queryset(self):
        return super(
            ActiveProgrammeManager, self).get_queryset().filter(is_active=True)


class EducationalProgramme(models.Model):
    institution = models.ForeignKey(
        Authority, related_name='related_edu_programmes')
    title = models.CharField(max_length=250)
    discipline = models.ForeignKey(Discipline)
    is_active = models.BooleanField()

    instructors = models.ManyToManyField(
        User, limit_choices_to={'groups': 7},
        help_text = "only persons from instructorsa group are available")  # group 7 instructors

    requires = models.ForeignKey("Course", blank=True, null=True)
    public = models.TextField(
        help_text="public to which programme is directed")

    summary = models.TextField()
    objective = models.TextField()
    achivement = models.TextField("knowledge acquired")
    #available_formats = models.TextField()
    certification = models.ForeignKey(
        CertificationProgramme, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="related_edu_programmes")

    # honoraries = models.DecimalField(
    #     max_digits=5, decimal_places=2,
    #     blank=True, null=True)

    active = ActiveProgrammeManager()

    def __unicode__(self):
        return "%s" % self.title


class Module(models.Model):
    educational_programme = models.ForeignKey(
        EducationalProgramme, related_name='related_modules')
    #name = models.CharField(max_length=250)
    hours = models.PositiveSmallIntegerField(
        blank=True, null=True)
    description = models.TextField(
        blank=True, null=True)
    observations = models.TextField(
        blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)

    def __unicode__(self):
        return "%s, %s" % (self.educational_programme, self.description)

    class Meta():
        verbose_name = "Didactic Module"
        verbose_name_plural = "Didactic Modules"


class ProgrammeResource(models.Model):
    TYPES = (
        (1, "didactic material - public"),
        (2, "didactic material - participants"),
        (3, "publicity"),
        (4, "administrative"),
    )
    course = models.ForeignKey(EducationalProgramme)
    title = models.CharField(max_length=250)
    file = models.FileField()
    type = models.PositiveSmallIntegerField(choices=TYPES)
    observations = models.TextField(
        blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)

    def __unicode__(self):
        return "%s, %s" % (self.course, self.title)


class ParticipantGroup(models.Model):
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return "%s" % self.name


class Fee(models.Model):
    CURRENCIES = (
        ("EUR", "Euros"),
        ("DOL", "Dollars"),
    )
    programme = models.ForeignKey(
        EducationalProgramme, related_name='related_fees')

    zone = models.ForeignKey(Zone)
    participant_group = models.ForeignKey(ParticipantGroup)

    currency = models.CharField(
        choices=CURRENCIES, max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)

    def __unicode__(self):
        return u"%s - %s - %s" % (
            self.programme, self.zone, self.participant_group)

    class Meta(object):
        unique_together = (("zone", "participant_group"))


class CourseQuerySet(models.QuerySet):
    def opened(self):
        return self.filter(status=2)

    def closed(self):
        return self.filter(status=3)


class CourseManager(models.Manager):
    def get_queryset(self):
        return CourseQuerySet(self.model, using=self._db)

    def opened(self):
        return self.get_queryset().opened()

    def closed(self):
        return self.get_queryset().closed()


class Course(models.Model):
    STATUS = (
        (1, "preparation"),
        (2, "recrutation"),
        (3, "finished"),
        (4, "cancelled"),
    )

    educational_programme = models.ForeignKey(
        EducationalProgramme, related_name='related_courses')
    title = models.CharField(
        max_length=250, help_text='original title')
    accreditation = models.ForeignKey(
        Accreditation, blank=True, null=True)

    organizer = models.ForeignKey(Authority, related_name='related_organizers')
    manager = models.ForeignKey(
        User, related_name='related_managers', verbose_name="coordinator",
        limit_choices_to={'groups': 8},
        help_text = "only persons from 'Course Coordinators' group are available")  

    professors = models.ManyToManyField(
        User, related_name='related_professors', verbose_name="instructors",
        limit_choices_to={'groups': 7},
        help_text = "only persons from 'Instructors' group are available.")  

    main_language = models.CharField(
        choices=LANGUAGES, default="English", max_length=50)
    second_language = models.CharField(
        choices=LANGUAGES, max_length=50,
        blank=True, null=True)

    location = models.ForeignKey(Location)

    begins = models.DateField()
    finish = models.DateField()
    timetable = models.TextField()

    min_nbr_participants = models.PositiveSmallIntegerField(
        blank=True, null=True)
    max_nbr_participants = models.PositiveSmallIntegerField(
        blank=True, null=True)
    recrutation_starts = models.DateField(
        blank=True, null=True)

    status = models.PositiveSmallIntegerField(
        choices=STATUS, default=1)
    observations = models.TextField(
        blank=True, null=True)

    poster = models.ImageField(
        upload_to="courses/posters",
        blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)

    inscription_url = models.URLField(
        blank=True, null=True)

    objects = CourseManager()

    def is_open(self):
        now = datetime.date.today()
        if self.begins < now:
            return False
        if self.status == 2 and not self.recrutation_starts:
            return True
        if self.status == 2 and self.recrutation_starts < now:
            return True
        else:
            return False

    def __unicode__(self):
        return u"%s - %s - %s" % (self.title, self.begins, self.status)


class Participant(models.Model):
    STATUS = (
        (1, "recruited"),
        (2, "participant"),
        (3, "completed"),
        (4, "aworded"),
    )

    person = models.ForeignKey(Student, verbose_name="student")
    course = models.ForeignKey(Course)

    payed = models.DecimalField(
        max_digits=5, decimal_places=2,
        blank=True, null=True)

    status = models.PositiveSmallIntegerField(
        choices=STATUS, default=1)
    certificate = models.ForeignKey(
        Certificate, null=True, blank=True)

    observations = models.TextField(
        blank=True, null=True)

    submitted_at = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return u"%s - %s - %s" % (self.course, self.person)

    class Meta(object):
        unique_together = (("course", "person"),)


class Communication(models.Model):
    TYPES = (
        (1, "didactic material"),
        (2, "publicity"),
        (3, "administrative"),
    )
    course = models.ForeignKey(Course)
    subject = models.CharField(max_length=250)
    text = models.TextField()
    file = models.FileField(
        null=True, blank=True)

    sent_at = models.DateField(auto_now_add=True)
    sent_by = models.ForeignKey(User)

    observations = models.TextField(
        blank=True, null=True)

    def __unicode__(self):
        return u"%s - %s - %s" % (self.course, self.sent_at, self.subject)

from django.db import models

from django.contrib.auth.models import User

from locations.models import Location
from persons.models import Person
from certifications.models import Accreditation, Certificate
from authorities.models import Authority


class Course(models.Model):
    STATUS = (
        (1, "preparation"),
        (2, "recrutation"),
        (3, "finished"),
        (4, "cancelled"),
    )

    title = models.CharField(max_length=250)
    requires = models.ForeignKey("Course", blank=True, null=True)
    summary = models.TextField()
    programme = models.TextField()

    accreditation = models.ForeignKey(
        Accreditation, blank=True, null=True)

    organizer = models.ForeignKey(Authority, related_name='related_organizers')
    manager = models.ForeignKey(User, related_name='related_managers')
    professors = models.ManyToManyField(User)

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

    budget = models.DecimalField(
        max_digits=5, decimal_places=2,
        blank=True, null=True)
    honoraries = models.DecimalField(
        max_digits=5, decimal_places=2,
        blank=True, null=True)
    expences = models.DecimalField(
        max_digits=5, decimal_places=2,
        blank=True, null=True)
    profit = models.DecimalField(
        max_digits=5, decimal_places=2,
        blank=True, null=True)

    poster = models.ImageField(upload_to="courses/posters")

    def __unicode__(self):
        return u"%s - %s - %s" % (self.title, self.begins, self.status)


class File(models.Model):
    TYPES = (
        (1, "didactic material"),
        (2, "publicity"),
        (3, "administrative"),
    )
    course = models.ForeignKey(Course)
    file = models.FileField()
    type = models.PositiveSmallIntegerField(choices=TYPES)
    observations = models.TextField(
        blank=True, null=True)


class Participant(models.Model):
    STATUS = (
        (1, "recruited"),
        (2, "participant"),
        (3, "completed"),
        (4, "aworded"),
    )

    person = models.ForeignKey(Person)
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

    submitted_at = models.DateField(auto_now_add=True)
    observations = models.TextField(
        blank=True, null=True)

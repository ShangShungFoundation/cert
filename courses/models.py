from django.db import models

from locations.models import Location
from persons.models import Person
from certifications.models import Accreditation


class Course(models.Model):
    STATUS = (
        (1, "in preparation"),
        (3, "cancelled"),
    )

    title = models.CharField(max_length=250)
    summary = models.TextField()

    accreditation = models.ForeignKey(
        Accreditation, blank=True, null=True)

    professor = models.ForeignKey(Person, related_name='related_profesors')
    organizer = models.ForeignKey(Person, related_name='related_organizers')

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

    status = models.PositiveSmallIntegerField(choices=STATUS)

    def __unicode__(self):
        return u"%s - %s - %s" % (self.name, self.place, self.country)


class File(models.Model):
    TYPES = (
        (1, "didactic material"),
        (2, "publicity"),
        (3, "administrative"),
    )
    course = models.ForeignKey(Course)
    file = models.FileField()
    type = models.PositiveSmallIntegerField(choices=TYPES)


class Participant(models.Model):
    person = models.ForeignKey(Person)
    course = models.ForeignKey(Course)

    submitted_at = models.DateField(auto_now_add=True)

    payed = models.DecimalField(
        max_digits=5, decimal_places=2,
        blank=True, null=True)

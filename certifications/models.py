import pycountry
from django.db import models

COUNTRIES = [(c.alpha2, c.name) for c in pycountry.countries]


class Certification(models.Model):
    """Certification refers to the confirmation of certain characteristics
    of an object, person, or organization.
    - https://en.wikipedia.org/wiki/Certification"""

    TYPES = (
        (1, "Achivement"),
        (2, "Aword"),
    )

    name = models.CharField(max_length=250)
    type = models.CharField(choices=TYPES, max_length=250)
    authority = models.ForeignKey("authorities.Authority")
    description = models.TextField(
        blank=True, null=True)
    requires = models.ForeignKey(
        "Certification",
        blank=True, null=True,
        help_text=u"""indicates if cerfiticate
        requires beforhead another certificate""")
    file = models.FileField(blank=True, null=True)

    def __unicode__(self):
        return u"%s - %s - %s" % (self.name, self.place, self.country)


class Location(models.Model):
    name = models.CharField(max_length=250)
    place = models.TextField()
    country = models.CharField(
        choices=COUNTRIES, max_length=5)

    def __unicode__(self):
        return u"%s - %s - %s" % (self.name, self.place, self.country)


class Accreditation(models.Model):
    """Accreditation is a specific organization's process of certification."""

    certification = models.ForeignKey(Certification)
    date = models.DateField()
    location = models.ForeignKey(Location)
    description = models.TextField(
        blank=True, null=True)

    def __unicode__(self):
        return u"%s %s at %s" % (self.certification, self.date, self.location)

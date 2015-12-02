from django.db import models
from django.contrib.auth.models import User

from locations.models import Location
from persons.models import Person


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
        requires pssesion of another certificate""")
    file = models.FileField(blank=True, null=True)

    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s - %s - %s" % (self.name, self.place, self.country)



class Accreditation(models.Model):
    """Accreditation is a specific organization's process of certification."""

    certification = models.ForeignKey(Certification)
    certifiers = models.ManyToManyField(
        'authorities.Certifier', related_name="related_certifiers")

    released_at = models.DateField()
    location = models.ForeignKey(Location)
    description = models.TextField(
        blank=True, null=True)

    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s %s at %s" % (self.certification, self.date, self.location)


class Certificate(models.Model):
    """Certification applied to the particular person"""

    person = models.ForeignKey(Person)
    accreditation = models.ForeignKey(Accreditation)

    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

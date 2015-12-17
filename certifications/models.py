from django.db import models
from django.contrib.auth.models import User

from locations.models import Location
from persons.models import Person


class Discipline(models.Model):
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return u"%s" % self.name


class CertificationProgramme(models.Model):
    """Certification refers to the confirmation of certain characteristics
    of an object, person, or organization.
    - https://en.wikipedia.org/wiki/Certification"""

    TYPES = (
        (1, "Achievement"),
        (2, "Aword"),
    )

    name = models.CharField(max_length=250)
    title = models.CharField("certificate title", max_length=250)
    cert_type = models.PositiveSmallIntegerField(choices=TYPES)

    authority = models.ForeignKey("authorities.Authority")

    discipline = models.ForeignKey(Discipline)
    summary = models.TextField()
    achivement = models.TextField()
    public = models.TextField(
        help_text="defines public to which certificate is targeted")
    requires = models.ForeignKey(
        "CertificationProgramme",
        blank=True, null=True,
        help_text=u"""indicates if ather certification rograme is necessary""")

    file = models.FileField(
        blank=True, null=True,
        help_text="certificate template")

    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.name


class Accreditation(models.Model):
    """Accreditation is a specific organization's process of certification."""

    certification = models.ForeignKey(
        CertificationProgramme, related_name="related_acreditations")
    certifiers = models.ManyToManyField(
        'authorities.Certifier', related_name="related_certifiers")

    released_at = models.DateField()
    location = models.ForeignKey(Location)
    description = models.TextField(
        blank=True, null=True)

    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        ordering = ("released_at",)

    def __unicode__(self):
        return u"%s at %s, %s" % (self.certification, self.location, self.released_at)


class Certificate(models.Model):
    """Certification applied to the particular person"""

    person = models.ForeignKey(Person)
    accreditation = models.ForeignKey(Accreditation)

    observations = models.TextField(blank=True, null=True)

    file = models.FileField(blank=True, null=True)

    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        unique_together = ("person", "accreditation")

    def __unicode__(self):
        return u"%s %s" % (self.person, self.accreditation)


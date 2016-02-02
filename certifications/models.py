from django.db import models
from django.contrib.auth.models import User

from locations.models import Location
from students.models import Student


class Discipline(models.Model):
    name = models.CharField(max_length=250)
    linage = models.CharField(
        blank=True, null=True,
        max_length=250)
    history = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name


class CertificationProgramme(models.Model):
    """Certification refers to the confirmation of certain characteristics
    of an object, person, or organization.
    - https://en.wikipedia.org/wiki/Certification"""

    TYPES = (
        (1, "Attendance"),
        (2, "Diploma"),
    )

    name = models.CharField(max_length=250)
    title = models.CharField("certificate title", max_length=250)
    cert_type = models.PositiveSmallIntegerField(choices=TYPES)

    authority = models.ForeignKey("authorities.Authority", verbose_name='released by')

    discipline = models.ForeignKey(Discipline)
    
    expiery = models.PositiveSmallIntegerField(
        blank=True, null=True,
        help_text='in years')

    summary = models.TextField()
    description = models.TextField()
    
    prerequisities = models.TextField(blank=True, null=True)
    achivement = models.TextField("habilitations & Competences")

    public = models.TextField(
        help_text="defines public to which certificate is targeted")
    requires = models.ForeignKey(
        "CertificationProgramme",
        blank=True, null=True,
        help_text=u"""indicates if other certification programe is necessary""")

    cert_template = models.FileField(blank=True, null=True,)

    certifiers = models.ManyToManyField(
        User, limit_choices_to={'groups': 7},
        help_text = "only persons from 'instructors' group are available")  

    created_by = models.ForeignKey(User, related_name='cert_creator')
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
    """Certification applied to the particular student"""

    student = models.ForeignKey(Student)
    accreditation = models.ForeignKey(Accreditation)

    observations = models.TextField(blank=True, null=True)

    file = models.FileField(blank=True, null=True)

    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        unique_together = ("student", "accreditation")

    def __unicode__(self):
        return u"%s %s" % (self.student, self.accreditation)


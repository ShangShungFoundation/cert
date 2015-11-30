from django.db import models

from certifications.models import Accreditation


class Authority(models.Model):
    """Describes institution issuing certification"""

    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name


class Certifier(models.Model):
    """Refers to person which authorize acreditation of certificate"""

    accreditation = models.ForeignKey(Accreditation)
    role = models.TextField()
    person = models.ForeignKey("persons.Person")

    def __unicode__(self):
        return u"%s %s" % (self.role, self.person)

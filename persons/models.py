import pycountry
from django.db import models

from certifications.models import Accreditation

COUNTRIES = [(c.alpha2, c.name) for c in pycountry.countries]


class Person(models.Model):
    """docstring for Person"""
    TREATMENTS = (
        ("Mr", "Mr"),
        ("Mrs", "Mrs"),
        ("Ms", "Ms"),
    )
    treatment = models.CharField(
        choices=TREATMENTS, max_length=50)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    birth = models.DateField()
    email = models.EmailField()
    tel = models.CharField(max_length=250)
    address = models.TextField()
    country = models.CharField(
        choices=COUNTRIES, max_length=50)

    def __unicode__(self):
        return u"%s %s %s" % (self.treatment, self.first_name, self.last_name)


class Certificate(models.Model):
    """Certification applied to the particular person"""

    person = models.ForeignKey(Person)
    issue = models.ForeignKey(Accreditation)

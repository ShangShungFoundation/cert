import pycountry

from django.db import models
from django.contrib.auth.models import User


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
    birth = models.DateField(null=True, blank=True)

    email = models.EmailField()
    tel = models.CharField(
        null=True, blank=True, max_length=250)

    address = models.TextField()
    country = models.CharField(
        choices=COUNTRIES, max_length=50)

    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s %s %s" % (self.treatment, self.first_name, self.last_name)



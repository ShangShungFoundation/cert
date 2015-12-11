import pycountry

from django.db import models

COUNTRIES = [(c.alpha2, c.name) for c in pycountry.countries]


class Zone(models.Model):
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return u"%s" % (self.name)


class Location(models.Model):
    zone = models.ForeignKey(Zone)
    name = models.CharField(max_length=250)
    place = models.TextField()
    country = models.CharField(
        choices=COUNTRIES, max_length=5)

    def __unicode__(self):
        return u"%s - %s - %s" % (self.name, self.place, self.get_country_display())


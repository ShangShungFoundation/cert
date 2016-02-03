from django.conf.urls import patterns, url
import certifications.views


urlpatterns = [
    url(r'^certificate/(?P<object_id>\d+)/$',
        certifications.views.certificate, name="certificate"),
    url(r'^certificates/(?P<certification_id>\d+)/$',
        certifications.views.certificates, name='certificates'),
    url(r'^certification/(?P<object_id>\d+)/$',
        certifications.views.certification, name='certification'),
    url(r'^accreditations/$',
        certifications.views.accreditations, name='accreditations'),
    url(r'^$',
        certifications.views.certifications, name='certifications'),
]
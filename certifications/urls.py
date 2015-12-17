from django.conf.urls import patterns, url
import certifications.views


urlpatterns = [
    url(r'^certificate/(?P<object_id>\d+)/$',
        certifications.views.certificate, name="certificate"),
    url(r'^certification/(?P<object_id>\d+)/$',
        certifications.views.certification, name='certification'),
    url(r'^certificates/(?P<certification_id>\d+)/$',
        certifications.views.certificates, name='certificates'),
    url(r'^$',
        certifications.views.certifications, name='certifications'),
]
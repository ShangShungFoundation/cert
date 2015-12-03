from django.conf.urls import patterns, url

urlpatterns = patterns('certifications.views',
    url(r'^certificate/(?P<object_id>\d+)/$',
        "certificate", name="certificate"),
    url(r'^certification/(?P<object_id>\d+)/$',
        "certification", name='certification'),
    url(r'^$',
        "certifications", name='certifications'),
)
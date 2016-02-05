from django.conf.urls import patterns, url
import courses.views


urlpatterns = [
    url(r'^course/(?P<object_id>\d+)/$',
        courses.views.course, name="course"),
    url(r'^open-courses/$',
        courses.views.open_courses, name='open_courses'),
    url(r'^(?P<object_id>\d+)/$',
        courses.views.programme, name='educational_programme'),
    url(r'^discipline/(?P<object_id>\d+)/$',
        courses.views.discipline, name='discipline'),
    url(r'^$',
        courses.views.programmes, name='educational_programmes'),
]

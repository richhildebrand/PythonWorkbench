from django.conf.urls import patterns, include, url
from UserCode import UserCodeManager

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'capstone.views.home', name='home'),
    # url(r'^capstone/', include('capstone.foo.urls')),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'capstone.student.views.index'),
    url(r'^student/$', 'capstone.student.views.index'),
    url(r'^student/startDebugging/$', 'capstone.student.views.startDebugging'),
    url(r'^student/takeStep/$', 'capstone.student.views.takeStep'),
)

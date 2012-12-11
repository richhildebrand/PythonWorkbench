from django.conf.urls import patterns, include, url
from UserCode import UserCodeManager

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PythonWorkbench.views.home', name='home'),
    # url(r'^PythonWorkbench/', include('PythonWorkbench.foo.urls')),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'PythonWorkbench.student.views.index'),
    url(r'^student/$', 'PythonWorkbench.student.views.index'),
    url(r'^student/startDebugging/$', 'PythonWorkbench.student.views.startDebugging'),
    url(r'^student/runAll/$', 'PythonWorkbench.student.views.runAll'),
    url(r'^student/takeStep/$', 'PythonWorkbench.student.views.takeStep'),
    url(r'^Exercise/displayAll/$', 'PythonWorkbench.Exercise.views.displayAll'),
    url(r'^Exercise/load/(?P<exerciseId>\d+)/$', 'PythonWorkbench.Exercise.views.load'),
)

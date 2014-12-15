# urls general

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'micrositios.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^micSitCeg/', include('micSitCeg.urls')),)

    url(r'^admin/', include(admin.site.urls)),
)

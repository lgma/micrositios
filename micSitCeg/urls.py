#urls de micSitCeg

from django.conf.urls import patterns, url

from micSitCeg import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
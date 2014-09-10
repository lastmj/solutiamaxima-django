from django.conf.urls import patterns, url

from privateworkshop import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)

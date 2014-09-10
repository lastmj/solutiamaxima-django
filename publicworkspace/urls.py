from django.conf.urls import patterns, url

from publicworkspace import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^import', views.importCategories, name='importCategories'),
	url(r'^(?P<categoryID>\d+)', views.displayCategory, name='displayCategory'),
	#url(r'^(?P<categoryName>([A-z]+[\w ]?)+)', views.displayCategory, name='displayCategory'),
)

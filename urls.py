from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#legalese and misc
	url(r'^universalterms/$', 'views.universal_terms'),
	url(r'^tutorial/$', 'views.tutorial'),

	#user authentication urls
	url(r'^accounts/login/$', 'views.login_view'),
	url(r'^accounts/auth/$', 'views.auth_view'),
	url(r'^accounts/logout/$', 'views.logout_view'),
	url(r'^accounts/register/$', 'views.register_user'),
	#url(r'^accounts/register_success/$', 'views.register_success'),

	#apps
	url(r'^privateworkshop/', include('privateworkshop.urls', namespace="privateworkshop")),
    url(r'^createproblem/', include('createproblem.urls', namespace="createproblem")),
    url(r'^publicproblem/', include('publicproblem.urls', namespace="publicproblem")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^publicworkspace/', include('publicworkspace.urls', namespace="publicworkspace")),
   	url(r'^$', 'publicworkspace.views.index'),
)

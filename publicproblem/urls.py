from django.conf.urls import patterns, url

from publicproblem import views

urlpatterns = patterns('', 
	url(r'^(?P<problem_id>\d+)$', views.caja, name='cajaInit'),
	url(r'^(?P<problem_id>\d+)(?P<authToken>.+)$', views.caja, name='cajole'),
	#url(r'^text/(?P<problem_id>\d+)(?P<authToken>.+)$', views.getCajoledProblemText, name='getCajoledProblemText'),
	#url(r'^problemTextAuthUrl/$', views.getCajoledProblemText, name='problemTextAuthUrl'),
	url(r'^cajaAuthUrl/$', views.caja, name='cajaAuthUrl'),
	url(r'^submitVerification/$', views.submitVerification, name='submitVerification'),
)

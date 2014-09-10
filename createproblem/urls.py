from django.conf.urls import patterns, url

from createproblem import views

urlpatterns = patterns('', 
    url(r'^submitpreview/$', views.submitPreview, name='submitPreview'),
    url(r'^submitproblem/$', views.submitProblem, name='submitProblem'),
	url(r'^(?P<categoryId>\d+)$', views.index, name='index'),
	url(r'^(?P<categoryId>\d+)/(?P<problemId>\d+)$', views.index, name='edit'),
	url(r'^javascript/(?P<problem_id>\d+)$', views.getJavaScript, name='getjavascript'),
)

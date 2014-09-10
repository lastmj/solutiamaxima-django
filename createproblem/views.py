import re
import os, binascii

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core import signing
from django.core.signing import TimestampSigner, Signer
from django.core.exceptions import ObjectDoesNotExist

from publicproblem.models import PublicProblem
from publicworkspace.models import Categories

@login_required
def index(request, categoryId=None, problemId=None):
	try:
		practiceProblem = PublicProblem.objects.get(title="temporary-problem-" + request.user.username)
	except ObjectDoesNotExist:
		practiceProblem = PublicProblem()
		practiceProblem.title = "temporary-problem-" + request.user.username
		practiceProblem.category = Categories.objects.get(title="temporary")
		practiceProblem.author = User.objects.get(username=request.user.username)
		practiceProblem.save()
		
	problem = None
	if problemId is not None:
	    problem = PublicProblem.objects.get(pk=problemId)
	    if request.user != problem.author:
		    return HttpResponse("you don't have permission to edit this problem")
	
	return render(request, "createproblem/index.html", {'id':practiceProblem.id, 'categoryId':categoryId, 'problem':problem, 'nextURLTemplateVariable':request.GET['nextURL']})
	
@login_required
def submitProblem(request):
    if request.POST['problemId'] != '':
        problem = PublicProblem.objects.get(pk=request.POST['problemId'])
        if request.user != problem.author:
            return HttpResponse("you don't have permission to edit this problem")
    else:
        problem = PublicProblem()
        problem.category = Categories.objects.get(pk=request.POST['categoryId'])
        problem.author = User.objects.get(username=request.user.username)

    problem.text = request.POST['textEditor']
    problem.javascript = request.POST['codeEditor']
    problem.title = request.POST['title']

    problem.save()

    return HttpResponseRedirect(request.POST['nextURL'])

@login_required
def submitPreview(request):
    problem = PublicProblem.objects.get(title="temporary-problem-" + request.user.username)

    problem.text = request.POST['problemText']
    problem.javascript = request.POST['problemJavaScript']

    problem.save()
    
    return HttpResponse()
    
@login_required
def getJavaScript(request, problem_id):
	problem = PublicProblem.objects.all().filter(pk=problem_id)[0]
	
	if request.user != problem.author:
		return "you don't have permission to edit this problem"
	
	return HttpResponse(problem.javascript)

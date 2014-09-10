from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from publicproblem.models import PublicProblem

@login_required
def index(request):
	current_user = request.user
	problems_list = PublicProblem.objects.all().filter(author=current_user).exclude(title__startswith='temporary-problem-')
	
	context = {"request":request, "problems_list": problems_list}
	
	return render(request, "privateworkshop/index.html", context)

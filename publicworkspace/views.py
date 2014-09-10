import os

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from publicproblem.models import PublicProblem
from publicworkspace.models import Categories

def index(request):
	context = {}
	return render(request, "publicworkspace/index.html", context)
	
def displayCategory(request, categoryID):
	theCategory = Categories.objects.get(pk=categoryID)
	parentList = []
	getParents(theCategory, parentList)
	categoriesList = Categories.objects.all().filter(parentCategory=theCategory, activated=True).order_by('position')
	problemsListTemp = PublicProblem.objects.all().filter(category=theCategory)
	
	problemsList = []
	for i in xrange(0, len(problemsListTemp), 2):
		if i + 1 >= len(problemsListTemp):
			tempList = [problemsListTemp[i]]
		else:
			tempList = [problemsListTemp[i], problemsListTemp[i+1]]
		problemsList.append(tempList)
		
	context = {"request":request, "parentList":parentList, "categoriesList": categoriesList, "problemsList": problemsList, "theCategoryId":theCategory.id, "activated":getattr(theCategory, "activated")}

	return render(request, "publicworkspace/categories-and-problems.html", context)

def getParents(theCategory, parentList):
	parent = theCategory.parentCategory
	
	if parent != None:
		getParents(parent, parentList)
	
	if parent != None:
		parentList.append(theCategory)
	else:
		parentList.append(theCategory)
	
	return

@login_required
def importCategories(request):
    file = open(os.environ['OPENSHIFT_DATA_DIR'] + '/categories', 'r')
    
    previousParent = None
    parentList = []
    parent = None
    
    for line in file:
        temp = line.split('*')
        
        try:
            parent = Categories.objects.get(title = temp[1], parentCategory=previousParent)
            if parent != previousParent:
                parentList.append(parent)
                previousParent = parent
        except Exception:
            if len(parentList) != 0:
                parentList.pop()
            counter = len(parentList)
            parentListCopy = parentList[:]
            for p in parentList:
                try:
                    parent = Categories.objects.get(title = temp[1], parentCategory=parentList[counter-1])
                    parentListCopy.append(parent)
                    previousParent = parent
                    break
                except Exception:
                    counter = counter - 1
                    parentListCopy.pop()
            parentList = parentListCopy[:]
        
        category = Categories()
        category.title = temp[0]
        category.parentCategory = parent
        category.position = temp[2]
        category.activated = True
        category.save()
        
    return HttpResponse('good job kid')

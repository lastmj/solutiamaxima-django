import re
import sys
import os, binascii

from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core import signing
from django.core.signing import TimestampSigner, Signer
from django.conf import settings

from publicproblem.models import PublicProblem

def caja(request, problem_id=None, authToken=None):
    signer = TimestampSigner()

    if request.GET.get('type') == 'getToken' and settings.ON_PYTHON_ANYWHERE == True:
        value = signer.sign(binascii.b2a_hex(os.urandom(15)))
        return HttpResponse("https://www.solutiamaxima.com/publicproblem/" + request.GET.get('id') + "/" + value)
    elif request.GET.get('type') == 'getToken' and settings.ON_PYTHON_ANYWHERE == False:
        value = signer.sign(binascii.b2a_hex(os.urandom(15)))
        return HttpResponse("/publicproblem/" + request.GET.get('id') + "/" + value)

    if authToken is None:
        value = signer.sign(binascii.b2a_hex(os.urandom(15)))
        publicProblem = PublicProblem.objects.get(pk=problem_id)
        
        verifiedByUser = False
        
        if publicProblem.verifiedBy1 is not None and publicProblem.verifiedBy1 == request.user:
        	verifiedByUser = True
        elif publicProblem.verifiedBy2 is not None and publicProblem.verifiedBy2 == request.user:
        	verifiedByUser = True
        elif publicProblem.verifiedBy3 is not None and publicProblem.verifiedBy3 == request.user:
        	verifiedByUser = True
        
        return render(request, "publicproblem/caja.html", {'verifiedByUser':verifiedByUser, 'request':request, 'token':value, 'id':problem_id, 'author':publicProblem.author.username, 'problem':publicProblem})
    else:
        try:
            #original = signer.unsign(authToken[1:], max_age=5)
            original = signer.unsign(authToken[1:])
        except signing.BadSignature:
            return HttpResponse("incorrect token")

    publicProblem = PublicProblem.objects.get(pk=problem_id)

    if publicProblem.title.startswith('temporary-problem-'):
        if publicProblem.title != 'temporary-problem-' + request.user.username:
            return HttpResponse("you don't have permission to view this problem")

    randomList = re.findall(r"(r\d+)", publicProblem.text)
    randomSet = set(randomList)

    publicProblem.text = re.sub(r'<span class="math-tex">(.+?)</span>', r"\1", publicProblem.text)
    publicProblem.text = re.sub(r'\\', r'\\\\', publicProblem.text)

    tempString = ""
    tempAssignValues = ""
    tempReplaceDivs = ""
    tempReplaceReg = ""

    for counter, s in enumerate(randomSet):
        tempString += "var " + s + " = {};\n"
        tempString += "tempArray.push(" + s + ");\n"
        tempAssignValues += s + " = tempArray[%d].value;\n" % counter
        tempReplaceDivs += "elementList = document.querySelectorAll('." + s + "'); for(var i=0; i < elementList.length;i++){elementList[i].innerHTML = tempArray[%d].value;\n" % counter
        tempReplaceReg += "tempString = tempString.replace(/" + s + "/g, tempArray[%d].value.toString());\n" % counter

    publicProblem.replaceReg = tempReplaceReg
    publicProblem.replaceDivs = tempReplaceDivs
    publicProblem.assignValues = tempAssignValues
    publicProblem.vars = tempString
    publicProblem.numRandom = len(randomSet)
    publicProblem.authorName = publicProblem.author

    #make javascript look nice in html
    publicProblem.code = publicProblem.javascript.replace('\n', "<br />")

    publicProblem.javascript = ";" + publicProblem.javascript

    #Turn all javascript variables into local variables
    variableList = re.findall(r'[;|\s*]([a-zA-Z_$][a-zA-Z0-9_$]*\s*=)', publicProblem.javascript)
    variableSet = set(variableList)

    for v in variableSet:
        publicProblem.javascript = re.sub(r'[;|^|\s*]' + v, "var " + v, publicProblem.javascript, 1)

    context = {"publicProblem": publicProblem}

    return HttpResponse(render_to_string("publicproblem/index.html", context))
    
def submitVerification(request):
	publicProblem = PublicProblem.objects.get(pk=request.POST['id'])
	
	if publicProblem.verifiedBy1 is None and publicProblem.verifiedBy1 != request.user:
		publicProblem.verifiedBy1 = request.user
	elif publicProblem.verifiedBy2 is None and publicProblem.verifiedBy1 != request.user:
		publicProblem.verifiedBy2 = request.user
	elif publicProblem.verifiedBy3 is None and publicProblem.verifiedBy1 != request.user:
		publicProblem.verifiedBy3 = request.user
		publicProblem.verified = True
		
	publicProblem.save()
	return HttpResponse()

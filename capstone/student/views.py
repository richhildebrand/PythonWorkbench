from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, RequestContext, loader
from capstone.UserCode import UserCodeManager

userCodeManager = UserCodeManager.UserCodeManager("user", 'a=7')

def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def startDebugging(request):
	userCode = request.GET['pythonCode']
	userCodeManager = UserCodeManager.UserCodeManager("user", userCode)
	stepResult = userCodeManager.executeStepInUserCode()
	return HttpResponse(stepResult)

def takeStep(request):
	response = 'no Exception'
	try:
		response = userCodeManager.executeStepInUserCode()
	except Exception, e:
		response = e
	return HttpResponse(response)

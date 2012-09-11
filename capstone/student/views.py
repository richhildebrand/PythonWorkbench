from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, RequestContext, loader
from capstone.UserCode import UserCodeManager

def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def startDebugging(request):
	userCode = request.GET['pythonCode']
	userCodeManager = UserCodeManager.UserCodeManager("user", userCode)
	result = userCodeManager.executeStepInUserCode()
	return HttpResponse(userCode + result)
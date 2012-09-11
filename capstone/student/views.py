from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, RequestContext, loader
from capstone.UserCode import UserManager

userManager = UserManager.UserManager()

def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def startDebugging(request):
	userCode = request.GET['pythonCode']
	userManager.createUserCodeManager('user', userCode);
	stepResult = userManager.executeStepInUserCode('user')
	return HttpResponse(stepResult)

def takeStep(request):
	stepResult = userManager.executeStepInUserCode('user')
	return HttpResponse(stepResult)

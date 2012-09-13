from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, RequestContext, loader
from capstone.UserCode import UserManager

userManager = UserManager.UserManager()

def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def startDebugging(request):
	userCode = request.GET['pythonCode']
	request.session.save() 
	sessionIdForAnonymousUser = 'AnonymousUserSession' + request.session.session_key
	userManager.createUserCodeManager(sessionIdForAnonymousUser, userCode);
	stepResult = userManager.executeStepInUserCode(sessionIdForAnonymousUser)
	return HttpResponse(stepResult)

def takeStep(request):
	sessionIdForAnonymousUser = 'AnonymousUserSession' + request.session.session_key
	stepResult = userManager.executeStepInUserCode(sessionIdForAnonymousUser)
	return HttpResponse(stepResult)

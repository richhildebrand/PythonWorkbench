import json
from django.utils import simplejson
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, RequestContext, loader
from PythonWorkbench.UserCode import UserManager

userManager = UserManager.UserManager()

def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def startDebugging(request):
	try:
		userCode = request.GET['pythonCode']
		unitTests = request.GET['unitTests']
		request.session.save() 
		sessionIdForAnonymousUser = 'AnonymousUserSession' + request.session.session_key
		userManager.createUserCodeManager(sessionIdForAnonymousUser, userCode, unitTests);
		stepResult = userManager.executeStepInUserCode(sessionIdForAnonymousUser)
		testResults = userManager.runTestsOnUserCode(sessionIdForAnonymousUser);
		stepResult['testResults'] = testResults
		return HttpResponse(json.dumps(stepResult), mimetype="application/json")
	except Exception, e:
		print "\n\nstartDebugging exception = " + str(e) + "\n\n"

def takeStep(request):
	sessionIdForAnonymousUser = 'AnonymousUserSession' + request.session.session_key
	stepResult = userManager.executeStepInUserCode(sessionIdForAnonymousUser)
	return HttpResponse(json.dumps(stepResult), mimetype="application/json")	
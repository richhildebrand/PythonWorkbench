import json
from django.utils import simplejson
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, RequestContext, loader
from PythonWorkbench.Exercise.models import Exercise
from PythonWorkbench.Exercise.models import MethodCall
from django.http import Http404

def displayAll(request):
	exerciseList = Exercise.objects.all()
	t = loader.get_template('exerciseView.html')
	c = Context({'exerciseList': exerciseList })
	return HttpResponse(t.render(c))

def load(request, exerciseId):
	exerciseDetails = {}
	methodCalls = {}
	try:
		requestedExercise = Exercise.objects.get(pk=exerciseId)
		exerciseDetails['MethodBody'] = requestedExercise.methodBody
		exerciseDetails['WordProblem'] = requestedExercise.wordProblem

		methodCallsForRequestedExercise = MethodCall.objects.filter(exercise=exerciseId)
		for methodCall in methodCallsForRequestedExercise:
			methodCalls[methodCall.methodCall] = methodCall.expectedResult
		exerciseDetails['MethodCalls'] = methodCalls

	except requestedExercise.DoesNotExist:
		raise Http404
	return HttpResponse(json.dumps(exerciseDetails), mimetype="application/json")
import json
from django.utils import simplejson
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, RequestContext, loader
from capstone.Exercise.models import Exercise
from django.http import Http404

def displayAll(request):
	exerciseList = Exercise.objects.all()
	t = loader.get_template('exerciseView.html')
	c = Context({'exerciseList': exerciseList })
	return HttpResponse(t.render(c))

def load(request, exerciseId):
	ExerciseDetails = {}
	try:
		requestedExercise = Exercise.objects.get(pk=exerciseId)
		ExerciseDetails['MethodBody'] = requestedExercise.methodBody
		ExerciseDetails['WordProblem'] = requestedExercise.wordProblem
	except requestedExercise.DoesNotExist:
		raise Http404
	return HttpResponse(json.dumps(ExerciseDetails), mimetype="application/json")
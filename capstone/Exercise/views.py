from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, RequestContext, loader

def displayExercises(request):
	print "inside displayExercises"
	try:
		from capstone.Exercise.models import Exercise
		exerciseList = Exercise.objects.all()
		t = loader.get_template('exerciseView.html')
		print "before declaring exerciseList"
		c = Context({'exerciseList': exerciseList })
		print "after declaring exerciseList"
		return HttpResponse(t.render(c))
	except Exception, e:
		return HttpResponse(e)
	return HttpResponse("hi")
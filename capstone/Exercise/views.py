from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, RequestContext, loader

def displayExercises(request):
	print "inside displayExercises"
	try:
		from capstone.Exercise.models import Exercise
		latest_poll_list = Exercise.objects.all().order_by('-pub_date')[:5]
		t = loader.get_template('exerciseView.html')
		c = Context({'exerciseList': exerciseList })
		return HttpResponse(t.render(c))
	except Exception, e:
		return HttpResponse(e)
	return HttpResponse("hi")
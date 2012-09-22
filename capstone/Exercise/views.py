from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, RequestContext, loader
from capstone.Exercise.models import Exercise

def displayAll(request):
	exerciseList = Exercise.objects.all()
	t = loader.get_template('exerciseView.html')
	c = Context({'exerciseList': exerciseList })
	return HttpResponse(t.render(c))
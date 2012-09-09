from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, RequestContext, loader
import pdb

def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def debugCode(request):
	page = request.POST['PythonCode']
	return HttpResponse(page)
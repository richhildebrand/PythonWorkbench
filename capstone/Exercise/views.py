from django.template import Context, loader
from Exercise.models import Exercise
from django.http import HttpResponse

def displayExercises(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('exerciseView.html')
    c = Context({
        'exerciseList': exerciseList,
    })
    return HttpResponse(t.render(c))
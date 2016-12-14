from django.shortcuts import render
from django.template import RequestContext

def index(request):
    return render('location/index.html', context_instance=RequestContext(request))

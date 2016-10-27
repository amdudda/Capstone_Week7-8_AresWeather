from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def MWindex(request):
    return HttpResponse("Hello, Mars explorers!  This will be the Mars weather database loader page!")
    # return render(request,'MWdatabase/index.html')
    # The first line works but the second one doesn't -- why?

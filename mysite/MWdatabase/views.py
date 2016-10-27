from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, Mars explorers!  This will be the Mars weather database loader page!")
    #return render(request,'MWdatabase/index.html')
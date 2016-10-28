from django.shortcuts import render
from django.http import HttpResponse
from .models import Weather

# Create your views here.

def index(request):
    # return HttpResponse("Hello, Mars explorers!  This will e a Mars weather explorer app!")
    # get the first available sol's worth of data and send it to the home page as its context
    weather = { 'weather': Weather.objects.order_by('-sol')[:1][0] }
    return render(request, 'marsweather/index.html', weather)
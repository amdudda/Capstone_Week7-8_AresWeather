from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Weather

# some useful globals
first_sol = Weather.objects.order_by('sol')[:1][0].sol
last_sol = Weather.objects.order_by('-sol')[:1][0].sol

# Create your views here.

def index(request):
    # return HttpResponse("Hello, Mars explorers!  This will e a Mars weather explorer app!")
    # get the first available sol's worth of data and send it to the home page as its context
    w = Weather.objects.order_by('sol')[:1][0]
    ns = int(w.sol) + 1
    if (ns > last_sol): ns = None
    ps = int(w.sol) - 1
    if (ps < first_sol): ps = None
    context = {'weather': w, 'next_sol': ns, 'prev_sol': ps}
    return render(request, 'marsweather/index.html', context)

def sol(request,sol_id):
    w = get_object_or_404(Weather, sol=sol_id)
    ns = int(w.sol) + 1
    if (ns > last_sol): ns = None
    ps = int(w.sol) - 1
    if (ps < first_sol): ps = None
    context = {'weather': w, 'next_sol': ns, 'prev_sol': ps}
    return render(request, 'marsweather/index.html', context)
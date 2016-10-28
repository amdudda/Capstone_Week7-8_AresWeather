from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
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
    ps = None
    dirp = ''
    context = {'weather': w, 'next_sol': ns, 'prev_sol': ps, 'dirp': dirp}
    return render(request, 'marsweather/index.html', context)

def sol(request,sol_id):
    w = None
    ns = int(sol_id) + 1
    ps = int(sol_id) - 1
    try:
        w = get_object_or_404(Weather, sol=sol_id)
        # w = Weather.objects.get(sol=sol_id)
        # # print(w)
        # ns = int(w.sol) + 1
        # ps = int(w.sol) - 1
    except w.DoesNotExist:
        # catch case where the sol does not have any data - just make sure w returns a sol so the web page displays it
        # I want to handle it this way in case someone decides to get creative with picking sols
        w = Weather(sol=sol_id)
    finally:
        dirp = "../"
        if (ns > last_sol): ns = None
        if (ps < first_sol): ps = None
        context = {'weather': w, 'next_sol': ns, 'prev_sol': ps, 'dirp': dirp}
        return render(request, 'marsweather/index.html', context)
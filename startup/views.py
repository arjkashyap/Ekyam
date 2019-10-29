from django.shortcuts import render
from .models import *

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    startups = Startup.objects.all()
    return render(request, 'startup/index.html', {'startups': startups})

class Add(CreateView):
    model = Startup
    fields = ['startup_img','startup_product', 'startup_name', 'startup_date', 'startup_sector', 'startup_team_size' , 'startup_desc']

class Team(CreateView):
    model = TeamBuild
    fields = ['name', 'project_name', 'project_description', 'skill_required', 'team_size']

@login_required
def jobs(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    jobs = TeamBuild.objects.all()
    return render(request, 'startup/jobs.html', {'jobs': jobs})

@login_required
def market(request):
    products = Startup.objects.all()
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    return render(request, 'startup/market.html', {'products': products})

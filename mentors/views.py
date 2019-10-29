from django.shortcuts import render
from .models import *
def index(request):
    mentors = Mentors.objects.all().exclude(verify = False)
    return render(request, 'mentors/index.html', {'mentors': mentors})

class Register(CreateView):
    model = Mentors
    fields = ['name', 'location', 'designation', 'expertise', 'description', 'image', 'resume']



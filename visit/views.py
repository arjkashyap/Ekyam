from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render
from visit.models import *
from .forms import UserRegistrationForm, LoginForm ,UserProfileForm
from django.urls import reverse
from django.views.generic import UpdateView
from django.views.generic import FormView
from django.shortcuts import render, get_object_or_404

def Registration(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form  = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username = form.cleaned_data['username'],email = form.cleaned_data['email'] , password = form.cleaned_data['password'])
            user.save()

            return HttpResponseRedirect('/')
        else:
            return render(request, 'visit/registration/register.html', {'form': form},)

    else:
        form= UserRegistrationForm()
        context = {'form': form}
        return render(request, 'visit/registration/register.html', context )


@login_required
def Profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    return render(request,'visit/profile.html')






class NewUserProfileView(FormView):
    template_name = "visit/user_profile.html"
    form_class = UserProfileForm

    def form_valid(self, form):
        form.save(self.request.user)
        return super(NewUserProfileView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse("main:home")





class EditUserProfileView(UpdateView):#Note that we are using UpdateView and not FormView
    model = UserProfile
    form_class = UserProfileForm
    template_name = "visit/user_profile.html"
    def get_object(self, *args, **kwargs):
        user1 = get_object_or_404(User, pk=self.kwargs['pk'])

        print(user1)
        # We can also get user object using self.request.user  but that doesnt work
        # for other models.

        return user1.userprofile

    def get_success_url(self, *args, **kwargs):
        return reverse("visit:user_profile")




def LoginRequest(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    if request.method == 'POST':
        form  = LoginRequest(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            UserProfile = authenticate(username=username, password=password)
            if UserProfile is not None:
                login(request, UserProfile)
                return HttpResponseRedirect('/profile/')
            else:
                return render(request,'visit/registration/login.html',{'form':form})
        else:
            return render(request, 'visit/registration/login.html', {'form': form})

    else:
        form= LoginForm()
        context = {'form': form}
        return render(request, 'visit/registration/login.html', context, )


def logoutRequest(request):
    logout(request)
    return  render(request, 'visit/index.html')


def index(request):
    return render(request, 'visit/index.html', context=None)
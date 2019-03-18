from django import forms
from . import  models
from .models import *
from django.contrib.auth.models import User   # fill in custom user info then save it



class UserRegistrationForm(forms.Form):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)



    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password']


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birth_date', 'state', 'gender', 'address', 'skill_sets') #Note that we didn't mention user field here.

    def save(self, user=None):
        user_profile = super(UserProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile



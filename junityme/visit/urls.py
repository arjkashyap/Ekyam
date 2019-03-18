from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'visit'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login/', auth_views.LoginView.as_view(), {'template_name': 'visit/registration/login.html'}, name='login'),
   # url(r'accounts/profile/', views.profile, name='profile'), # need to change the app directory from here
    url(r'^register/$', views.Registration, name='registration'),
    url(r'^profile/$', views.Profile, name='profile'),
    url(r'^logout/', views.logoutRequest, name='logout'),
    url(r'^profiles/new/(?P<pk>\d+)/$', NewUserProfileView.as_view(), name="new-user-profile"),
    url(r'^users/(?P<pk>\d+)/edit/', EditUserProfileView.as_view(), name="edit-user-profile"),

]

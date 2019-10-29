from django.conf.urls import url
from . import views

app_name = 'startup'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'add-startup/', views.Add.as_view(), name = 'add'),
    url(r'build-team/', views.Team.as_view(), name = 'team'),
    url(r'jobs/', views.jobs, name = 'jobs'),
    url(r'market/', views.market, name = 'market'),
]
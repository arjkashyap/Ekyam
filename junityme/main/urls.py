from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    url(r'^home/', views.home, name='home'),    # Home page
    url(r'incubators/$', views.incubators, name='incubators'),    # Incubator list page
    url(r'about/', views.about, name='about'),          # Websie about page
    url(r'results', views.result, name = 'result'),         # For search function
    url(r'incubators/(?P<incubator_id>[0-9]+)/', views.details, name = 'details'),      # shows details of incubators
    url(r'incubators/add-incuabtor/$', views.AddIncubator.as_view(), name = 'add-incubator'),     # Adding Inc
    url(r'/add-details/', views.AddDetails.as_view(), name = 'add-details'), #for additional details
    url(r'news/', views.news, name = 'news'),
    url(r'added/', views.added, name = 'added'),      #your incubator will be added soon page
    url(r'apply/', views.apply, name = 'apply'),
    url(r'done/', views.done, name = 'done'),
    url(r'location/', views.location, name = 'location'),
    url(r'prediction/', views.prediction, name = 'prediction'),
    url(r'^locate/(?P<pk>\d+)/$', views.locate, name = 'locate'),     # In this urls
    url(r'^startups/$', views.startups, name = 'startups'),
]


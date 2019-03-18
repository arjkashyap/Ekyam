from django.conf.urls import url
from . import views

app_name = 'mentors'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'register/', views.Register.as_view(), name = 'register'),
]
from django.conf.urls import url
from . import views

app_name = 'enetwork'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'post-question', views.Addquestions.as_view(), name = 'post-question'),
    url(r'list-question', views.QuestionList, name='list-question'),
]
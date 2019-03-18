from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class Question(models.Model):
    CATEGORY = (
        ('Technical/software', 'Technical/software'),
        ('Government Ministry', 'Government Ministry'),
        ('Hardware', 'Hardware'),
        ('Business', 'Business'),
        ('Management', 'management'),
    )



    problem_title = models.CharField(max_length=30)
    problem_description = models.TextField(max_length=2500)
    problem_category = models.CharField(max_length=50, choices=CATEGORY)
    problem_field = models.CharField(max_length=200)



    def get_absolute_url(self):
        return reverse('enetwork:index')




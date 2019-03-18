from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class Mentors(models.Model):
    name = models.CharField(max_length = 20)
    location = models.CharField(max_length = 20)
    designation = models.CharField(max_length = 20, default = 'CEO/CFO at XYZ')
    expertise = models.CharField(max_length = 30, default = 'Buisness Development, Content etc.')
    description = models.TextField(max_length= '1000', default = 'Give a brief about yourself')
    image = models.FileField()
    resume = models.FileField()
    verify = models.BooleanField(default = False)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('mentors:index')




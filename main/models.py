from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from datetime import date

class Incubators(models.Model):      # These are our database files for the Incubator Portal
    incubator_name = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    city_location = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    logo = models.FileField()
    verify = models.BooleanField(default = False)
    latt = models.FloatField(default = 30)
    lonn = models.FloatField(default = 25)

    def get_absolute_url(self):
        return reverse('main:added')

    def __str__(self):                  # Displays the following  stuff when a query is made
      return self.incubator_name + '-' + self.owner 

class Details(models.Model):
    incubator = models.ForeignKey(Incubators, on_delete = models.CASCADE, related_name='banana_pudding')    
    inc_name = models.CharField(max_length = 30)
    inc_img = models.FileField()
    inc_contact = models.CharField(max_length = 600, default = "Enter all available means of contacting")
    inc_details = models.TextField(max_length= 2500)
    inc_address = models.TextField(max_length = 600, default = "Address")
    inc_doc = models.FileField()
    inc_policy = models.FileField()

    def __str__(self):
        return self.inc_name



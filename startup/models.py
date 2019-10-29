from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import reverse
from datetime import date

class Startup(models.Model):
    startup_name = models.CharField(max_length = 30)
    startup_product = models.CharField(max_length = 30)
    startup_company = models.CharField(default = 'cp name', max_length = 100)
    startup_date = models.CharField(default = 'format = dd/mm/yyyy', max_length = 20)
    startup_sector = models.CharField(max_length = 30)
    startup_team_size = models.IntegerField(validators = [MaxValueValidator(6), MinValueValidator(0)])
    startup_desc = models.TextField(max_length=1200)
    startup_img = models.FileField(default = 'img')
    def __str__(self):
        return self.startup_name

    def get_absolute_url(self):
        return reverse('startup:index')

class TeamBuild(models.Model):
    name = models.CharField(max_length = 30)
    project_name = models.CharField(max_length = 30)
    project_description = models.TextField(max_length= 2500)
    skill_required = models.CharField(max_length = 200)
    team_size = models.IntegerField(default = 6)
 
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('startup:index')
        


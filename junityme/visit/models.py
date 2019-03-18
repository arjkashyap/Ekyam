import uuid
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser



class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    USER_TYPE = (
        ('Entrepreneur', 'Entrepreneur'),
        ('Mentor', 'Mentor'),
        ('Investor', 'Investor'),
        ('Job seeker', 'Job Seeker'),
    )

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    birth_date=models.DateField(default= None, null = True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    address = models.CharField(max_length=150)
    locality = models.CharField(max_length=30)
    state = models.CharField(max_length=30, default='Enter State')
    postal_code_4 = models.PositiveIntegerField(null=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE)
    skill_sets = models.CharField(max_length=150, default= 'Example:Computer Literacy/Information Technology/Business Experties')
    activation_key = models.CharField(max_length=64, verbose_name=u"Activation key",default=uuid.uuid1())
    is_verified = models.BooleanField(default=False)
    profile_photo = models.FileField(default = None, null = True)
    cover_photo = models.FileField(default=None, null=True)

    def __unicode__(self):
        return u"%s" % self.user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)



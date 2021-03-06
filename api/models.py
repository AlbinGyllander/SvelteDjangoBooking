from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

experienceLevel = [
    ('0', 'Beginner'),
    ('1', 'Intermidiate'),
    ('2', 'Advanced'),
    ('3', 'Trainer'),
]
tennisClubs = [
    ('0', 'SALK'),
    ('1', 'Kungliga Tennis Planen'),
    ('2', 'Solna Tennis Klubb'),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,editable=False)
    bio = models.TextField(max_length=500, blank=True)
    tennisClub = models.CharField(max_length=30, blank=True,default='' ,choices=tennisClubs)
    birth_date = models.DateField(null=True, blank=True)
    age= models.IntegerField(null=True,blank=True)
    experienceStatus = models.CharField(blank=True,max_length=30,default='B', choices=experienceLevel)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
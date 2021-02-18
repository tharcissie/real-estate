from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='images/', default='a.png')

    def __str__(self):
        return self.user.username
         

class Sector(models.Model):
    name  = models.CharField(max_length=100, unique=True)
    price = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return self.name



class District(models.Model):
    name  = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name




class House( models.Model):

    BRICKS = (
        ('mud','mud'),
        ('cement','cement'),
        ('brown','brown'),
    )

    ACTION = (
        ('renting','renting'),
        ('selling','selling'),
    )

    name    = models.CharField(max_length=800)
    description    = models.TextField(blank=True, null=True,)
    image      = models.ImageField(upload_to='contents',null=True)
    district    = models.ForeignKey(District, on_delete=models.CASCADE)
    sector    = models.ForeignKey(Sector, on_delete=models.CASCADE)
    published_date = models.DateField(auto_now_add=True)
    brick_type = models.CharField(max_length=10, choices=BRICKS, default='mud')
    house_size = models.PositiveIntegerField(default=0)
    plot_size = models.PositiveIntegerField(default=0)
    action = models.CharField(max_length=10, choices=ACTION, default='renting')
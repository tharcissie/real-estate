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
    count = models.PositiveIntegerField(default=0)
    mean = models.PositiveIntegerField(default=0)
    min = models.PositiveIntegerField(default=0)
    max = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return self.name



class District(models.Model):
    name  = models.CharField(max_length=100, unique=True)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




class House( models.Model):

    BRICKS = (
        ('type1','type1'),
        ('type2','type2'),
        ('type3','type3'),
    )

    ACTION = (
        ('renting','renting'),
        ('selling','selling'),
    )

    name    = models.CharField(max_length=800)
    description    = models.TextField(blank=True, null=True,)
    image      = models.ImageField(upload_to='contents',null=True)
    district    = models.ForeignKey(District, on_delete=models.CASCADE)
    published_date = models.DateField(auto_now_add=True)
    brick_type = models.CharField(max_length=10, choices=BRICKS, default='type1')
    house_size = models.PositiveIntegerField(default=0)
    plot_size = models.PositiveIntegerField(default=0)
    action = models.CharField(max_length=10, choices=ACTION, default='renting')
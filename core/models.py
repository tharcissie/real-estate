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
         

class House( models.Model):

    ACTION = (
        ('renting','renting'),
        ('selling','selling'),
    )

    TYPE = (
        ('house','house'),
        ('apartment','apartment'),
    )

    house_type    = models.CharField(max_length=800,choices=TYPE, default='house')
    description    = models.TextField(blank=True, null=True,)
    image      = models.ImageField(upload_to='contents',null=True)
    image1      = models.ImageField(upload_to='contents',null=True)
    image2     = models.ImageField(upload_to='contents',null=True)
    image3     = models.ImageField(upload_to='contents',null=True)
    image4     = models.ImageField(upload_to='contents',null=True)
    district    = models.CharField(max_length=800)
    sector    = models.CharField(max_length=800)
    published_date = models.DateField(auto_now_add=True)
    bed_rooms = models.PositiveIntegerField(default=0)
    bath_rooms = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    action = models.CharField(max_length=10, choices=ACTION, default='renting')

    def __str__(self):
        return self.house_type

    class Meta:
        ordering = ["-pk"]

    @classmethod
    def search_house(cls,search):
    	house = cls.objects.filter(house_type__icontains=search)
    	return house
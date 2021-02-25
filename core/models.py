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
        ('renting','Renting'),
        ('selling','Selling'),
    )

    TYPE = (
        ('house','House'),
        ('apartment','Apartment'),
    )

    type    = models.CharField(max_length=800,choices=TYPE, default='House')
    description    = models.TextField(blank=True, null=True,)
    image      = models.ImageField(upload_to='contents',null=True)
    image1      = models.ImageField(upload_to='contents',null=True)
    image2     = models.ImageField(upload_to='contents',null=True)
    image3     = models.ImageField(upload_to='contents',null=True)
    image4     = models.ImageField(upload_to='contents',null=True)
    district    = models.CharField(max_length=800)
    sector    = models.CharField(max_length=800)
    published_date = models.DateField(auto_now_add=True)
    beds = models.PositiveIntegerField(default=0)
    baths = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    action = models.CharField(max_length=10, choices=ACTION, default='Renting')
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name='Houses')

    def __str__(self):
        return self.type

    class Meta:
        ordering = ["-pk"]

    @classmethod
    def search_house(cls,search):
    	house = cls.objects.filter(type__icontains=search)
    	return house
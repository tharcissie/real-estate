from django.db import models
from datetime import datetime
from manager.models import Manager


# Create your models here.

class Listing(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    sector = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    brick_type = models.CharField(max_length=10, choices=BRICKS, default='mud')
    price = models.IntegerField()
    house_size = models.PositiveIntegerField(default=0)
    plot_size = models.PositiveIntegerField(default=0)
    published_date = models.DateField(auto_now_add=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
 
    def __str__(self):
        return self.title

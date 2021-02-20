from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    houses = House.objects.all()
    context={
        'houses':houses
    }
    return render(request, 'home.html',context)


def house_details(request, pk):
    house = Content.objects.get(pk = pk)
    context = {
        'house':house
    }
    return render(request, 'house_details.html', context)



def house_rent(request):
    houses = House.objects.filter(action='renting').order_by('-pk')
    context={
        'houses':houses
    }
    return render(request, 'house_rent.html',context)

def house_sell(request):
    houses = House.objects.filter(action='selling').order_by('-pk')
    context={
        'houses':houses
    }
    return render(request, 'house_sell.html',context)


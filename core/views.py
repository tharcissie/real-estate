from django.shortcuts import render
from .models import *
from .filters import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def home(request):
    houses = House.objects.all()
    house_filter = HouseFilter(request.GET, queryset = houses)
    context = {
        'filter':house_filter
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

def search_house(request):
    if 'house' in request.GET and request.GET["house"]:
        search = request.GET.get("house")
        house = House.search_house(search)
        message = f"{search}"
        context = {"house":house, 'search':search}
        return render(request, 'result.html',context)
    else:
        message = "You haven't searched for any term"
        return render(request, 'result.html',{"message":message})


from django.urls import path, include
from .views import *

urlpatterns = [
   path('', home, name = 'home'),
   path('signup/', signup, name='signup'),
   path('search/', search_house, name='search'),
]
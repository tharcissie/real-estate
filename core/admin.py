from django.contrib import admin
from .models import Sector, District, Profile, House

admin.site.register(Sector)
admin.site.register(Profile)
admin.site.register(District)
admin.site.register(House)
from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_data', 'manager')
    list_display_links = ('id', 'title')
    list_filter = ('manager',)
    list_editable = ('is_published',)
    
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)

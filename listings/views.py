from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import district_choices, sector_choices

# Create your views here.


def index(request):
    listings = Listing.objects.order_by('-list_data').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing=get_object_or_404(Listing, pk=listing_id)

    context={
        'listing':listing
    }

    return render(request, 'listings/listing.html', context)

# @login_required(login_url='/accounts/login/')
# def search(request):
#     queryset_list=Listing.objects.order_by('-list_data')

#     #keywords
#     if 'keywords' in request.GET:
#         keywords = request.GET['keywords']
#         if keywords:
#             queryset_list = queryset_list.filter(description__icontains = keywords)
        
#    #District
#     if 'district' in request.GET:
#         district = request.GET['district']
#         if district:
#             queryset_list=queryset_list.filter(district__iexact = district)

#      #sector
#     if 'sector' in request.GET:
#         sector = request.GET['sector']
#         if state:
#             queryset_list=queryset_list.filter(sector__iexact = sector)
    
                
#     context={
#         'sector_choices':sector_choices,
#         'district_choices':district_choices,
#         'listings':queryset_list,
#         'values':request.GET,
#     }

#     return render(request, 'listings/search.html', context)

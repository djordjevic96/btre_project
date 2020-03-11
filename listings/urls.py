from django.urls import path,include

from . import views

#listing/
urlpatterns = [
    path('',views.index,name='listings'), #/listings 
    path('<int:listing_id>',views.listing,name='listing'),
    path('search',views.search,name='search'),
]
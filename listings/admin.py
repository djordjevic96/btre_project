from django.contrib import admin

# Register your models here.
from .models import Listing

#show in admin area
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','list_date','realtor')
    list_display_links=('id','title')
    list_filter = ('realtor',) #because is one value!
    list_editable = ('is_published',)
    search_fields = ('title','description','address','city', 'state','zipcode','price')#search by
    list_per_page = 25
    


admin.site.register(Listing, ListingAdmin)

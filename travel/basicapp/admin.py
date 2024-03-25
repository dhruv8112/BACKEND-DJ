
# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import destination, Place ,sliderImage,contactModel,reviewModel

class DestinationAdmin(admin.ModelAdmin):
    list_display = ('Dest_Name', 'Dest_Desc', 'Dest_Img',)

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('State', 'Place_Name','Day','Night', 'Place_price',)  

class sliderAdmin(admin.ModelAdmin):
    list_display = ('sliderName', 'sliderParent')
    
class contactAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Contact')

class reviewAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Subject')

admin.site.register(destination, DestinationAdmin) 
admin.site.register(Place, PlaceAdmin) 
admin.site.register(sliderImage, sliderAdmin) 
admin.site.register(contactModel, contactAdmin)
admin.site.register(reviewModel, reviewAdmin)

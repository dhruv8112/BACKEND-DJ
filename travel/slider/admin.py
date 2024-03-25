from django.contrib import admin

# Register your models here.
from .models import slider

class sliderAdmin(admin.ModelAdmin):
    list_display=['title']

admin.site.register(slider,sliderAdmin)
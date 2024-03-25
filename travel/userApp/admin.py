from django.contrib import admin
from .models import userModel

class userAdmin(admin.ModelAdmin):
    list_display = ('userUsername', 'userContact')

admin.site.register(userModel, userAdmin)

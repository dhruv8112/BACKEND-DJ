from django.shortcuts import render
from models import slider
# Create your views here.
def slider_view(request):
    sliderShow=slider.objects.all()
    
    return render(request,'index.html',{'sliderGet':sliderShow})
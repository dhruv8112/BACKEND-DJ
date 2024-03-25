from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from .models import destination,contactModel,Place,reviewModel


from django.contrib.auth import authenticate, login as auth_login
def index(request):
    Place=destination.objects.all()  
    Review=reviewModel.objects.all().order_by('?')[:3]
    return render(request, 'index.html', {'destinations': Place,'review':Review})

def pakage(request, DestGet):
    try:
        pakageState = get_object_or_404(destination, Dest_Name=DestGet)
        places = Place.objects.filter(State=pakageState)
        return render(request, 'pakage.html', {'destination': pakageState, 'places': places})
    except destination.DoesNotExist:
        messages.error(request, 'This category does not exist')
        return render(request, 'pakage.html')
    
def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact')
        message = request.POST.get('message')
        print(name, email, contact_number, message)

        show_contact = contactModel.objects.create(  # Adjust the model name here
            Name=name,
            Email=email,
            Contact=contact_number,
            Message=message
        )

        show_contact.save()
        return HttpResponse("Contact created successfully")

    return render(request, 'contact.html')

def pakageDetails(request):
    pakageShow=Place.objects.all()
    return render(request, 'pakageDetails.html',{'pakageShow':pakageShow})

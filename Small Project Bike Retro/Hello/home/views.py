from django.shortcuts import render
from django.contrib import messages
from home.models import Contact
from django.contrib import messages
def garage(request):
    return render(request, 'garage.html')

def heritage(request):
    return render(request, 'heritage.html')

def workshop(request):
    return render(request, 'workshop.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        inquiry_type = request.POST.get('service')  # matches name="service" in contact.html
        bike_details = request.POST.get('bike_details')
        message = request.POST.get('message')

        contact_entry = Contact(
            name=name,
            email=email,
            phone=phone,
            inquiry_type=inquiry_type,
            bike_details=bike_details,
            message=message
        )
        contact_entry.save()
        messages.success(request, 'Your dispatch has been received! The workshop will get back to you shortly.')

    return render(request, 'contact.html')
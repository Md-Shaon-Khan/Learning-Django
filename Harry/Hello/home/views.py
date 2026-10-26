from django.shortcuts import render

def garage(request):
    return render(request, 'garage.html')

def heritage(request):
    return render(request, 'heritage.html')

def workshop(request):
    return render(request, 'workshop.html')

def contact(request):
    return render(request, 'contact.html')
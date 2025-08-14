from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse("Welcome to GatePass app")

def about(request):
    return HttpResponse("Wanna know about GatePass?")

def contact(request):
    return render(request, template_name='contact.html', context={'name': "BramTech"})
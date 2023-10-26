#from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

#from smsproject.adminapp.models import Admin

def demofunction(request):
    return HttpResponse("Pfsd Sdp Project")

def demofunction1(request):
    return HttpResponse("<h3>Skill week</h3>")

def demofunction2(request):
    return HttpResponse("<font color='pink' >Student Academics </font>")

def homefunction(request):
    return render(request,"index.html")

def aboutfunction(request):
    return render(request,"about.html")

def loginfunction(request):
    return render(request,"login.html")

def contactfunction(request):
    return render(request,"contact.html")



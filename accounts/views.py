from django.shortcuts import render
from .models import UserProfile,User
# Create your views here.
def addeducation(request):
    return render(request,'accounts/addeducation.html',{})
    
def addexperience(request):
    return render(request,'accounts/addexperience.html',{})
    
def createprofile(request):
    return render(request,'accounts/createprofile.html',{})
    
def dashboard(request):
    return render(request,'accounts/dashboard.html',{})
    
def login(request):
    return render(request,'accounts/login.html',{})
    
def profile(request):
    a=UserProfile.objects.get(id=1)
    return render(request,'accounts/profile.html',{'a':a})
    
def profiles(request):
    return render(request,'accounts/profiles.html',{})
    
def register(request):
    return render(request,'accounts/register.html',{}) 
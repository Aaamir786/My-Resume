from django.shortcuts import render
from django.http import HttpResponse 
#from .models import contact

# Create your views here.

def home(request):
    context = {'home':'active'}
    return render(request,'home.html',context)

def skill(request):
    context = {'skill':'active'}
    return render(request,'skill.html',context)

def contact(request):
    context = {'contact':'active'}
    return render(request,'contact.html',context)


def work(request):
    context = {'work':'active'}
    return render(request,'work.html',context)

def hire(request):
    
    return render(request,'hire.html')    
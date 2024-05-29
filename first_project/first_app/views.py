from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_index(request):
    return HttpResponse("Hello World!")

def index(request):
    return render(request, 'first_app/index.html')

def help(request):
    helpdict = {'help_inserts':'HELP PAGE'}
    return render(request,'first_app/help.html',context=helpdict)
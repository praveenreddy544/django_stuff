from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from mydb.models import Tpi
# Create your views here.

'''def demolist(request):
    chintulist_welcome_dict={'wtext':'Come on chintu'}
    all_tasks_you_posted = Tpi.objects.all
    chintulist_welcome_dict['tasks_overall']=all_tasks_you_posted
    return render(request,'two.html',chintulist_welcome_dict)
    #return HttpResponse('Welcome dhdh page')'''

def chklist(request):
    return HttpResponse('chklist')

def demlist(request):
    chintulist_welcome_dict={'wtext':'Come on chintu'}
    all_tasks_you_posted = Tpi.objects.all
    chintulist_welcome_dict['tasks_overall']=all_tasks_you_posted
    return render(request,'two.html',chintulist_welcome_dict)
    #return HttpResponse('demlist')


# Create your views here.

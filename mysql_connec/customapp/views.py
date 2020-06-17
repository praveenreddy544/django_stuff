from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from customapp.models import Authors
# Create your views here.

def demolist(request):
    chintulist_welcome_dict={'wtext':'Come on chintu'}
    all_tasks_you_posted = Authors.objects.all
    chintulist_welcome_dict['tasks_overall']=all_tasks_you_posted
    return render(request,'two.html',chintulist_welcome_dict)
    #return HttpResponse('Welcome dhdh page')
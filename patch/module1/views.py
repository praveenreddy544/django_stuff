from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from module1.models import Tpi

def chklist(request):
    return HttpResponse('chklist')

# Create your views here.

def demlist(request):
    chintulist_welcome_dict={'wtext':'Come on chintu'}
    all_tasks_you_posted = Tpi.objects.all()
    chintulist_welcome_dict['tasks_overall']=all_tasks_you_posted
    print(chintulist_welcome_dict['tasks_overall'])
    print('test')
    #print(chintulist_welcome_dict['tasks_overall']['servername'])
    return render(request,'four.html',chintulist_welcome_dict)
    #return render(request,'test.html',chintulist_welcome_dict)

    #return render(request,'test.html')
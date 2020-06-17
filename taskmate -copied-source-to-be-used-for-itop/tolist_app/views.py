from django.shortcuts import render,redirect
from django.http import HttpResponse
from tolist_app.models import Tasklist
from tolist_app.forms import TaskForm
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def todolist(request):
    return HttpResponse('Welcome tochintu page')

def demolist(request):
    return HttpResponse('Demo')

chintulist_welcome_dict={'welcome_texting':'Welcome Page chintu','chinnu':'chintu'}
contactlist_dict={'cnt_texting':'Contact page'}
aboutlist_dict={'abo_texting':'About list'}
filtered_results={}

def chintulist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            #form.save()
            print('Form is validate')
        data = request.POST.copy()
        query= data.get('task')
        blog= Tasklist.objects.all()
        #if query is not None:
        blog = blog.filter(

            Q(task__icontains=query) |
            Q(done__icontains=query) 
            )
        context = {
             "tasks_overall": blog,
        } 
        #trick = Tasklist.objects.get(task=entered_name)


        print(f"Found data is {context}")
        print(f"type of context is {type(context)}")
        #print(f"type is {type(trick)}")
        #filtered_results['got_data']=trick

        #print(f"FILTERED is {filtered_results}")



        #for i in trick:
            #print(f"Individual element is {i}")

        #print(f" Entered name is {entered_name}")

        #messages.success(request,("New task added!"))

        #print('post req ----->')
        #return redirect(chintulist)
        #return render(request,'html/filtered.html',context)
        return render(request,'html/home.html',context)
        #print('post req ----->')
        #return HttpResponse('dat')


    else:
        #return HttpResponse('retry')
        all_tasks_you_posted = Tasklist.objects.all()
        print(f"all_tasks_found is {all_tasks_you_posted}")
        print(f"type is {type(all_tasks_you_posted)}")

        print('chintu ana')
        print(all_tasks_you_posted)

        chintulist_welcome_dict['tasks_overall']=all_tasks_you_posted
            #return HttpResponse('chintu called list by him')
            #return render(request,'html/home.html',{})
        return render(request,'html/home.html',chintulist_welcome_dict)
            #return render(request,'one.html',{})'''

    '''else:
        all_tasks_you_posted = Tasklist.objects.all

        print('chintu ana')
        print(all_tasks_you_posted)

        chintulist_welcome_dict['tasks_overall']=all_tasks_you_posted
            #return HttpResponse('chintu called list by him')
            #return render(request,'html/home.html',{})
        return render(request,'html/home.html',chintulist_welcome_dict)
            #return render(request,'one.html',{})'''

    '''else:
        request HttpResponse('Retry')'''

def contactlist(request):
    #return render(request,'html/contact.html',{})
    return render(request,'html/contact.html',contactlist_dict)

def aboutlist(request):
    #return render(request,'html/about.html',{})
    return render(request,'html/about.html',aboutlist_dict)

'''def got_results(request):
    all_objs=Tasklist.objects.all
    print('calling all_objs')
    return render(request,'html/home2.html',{'call_objs':all_objs})'''

def deletelist(request,task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.delete()

    return redirect(chintulist)
from django.shortcuts import render,redirect
from django.http import HttpResponse
from tolist_app.models import Tasklist
from tolist_app.forms import TaskForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

def todolist(request):
    return HttpResponse('Welcome tochintu page')

def demolist(request):
    return HttpResponse('Demo')

chintulist_welcome_dict={'welcome_texting':'Welcome Page chintu','chinnu':'chintu'}
contactlist_dict={'cnt_texting':'Contact page'}
aboutlist_dict={'abo_texting':'About list'}
filtered_results={}

@login_required
def chintulist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            intermediate_form_step =  form.save(commit=False)
            intermediate_form_step.managed_by_user = request.user
            intermediate_form_step.save()
            #form.save()
            #print('Form is validate')
        '''#data = request.POST.copy()
        #query= data.get('task')
        #blog= Tasklist.objects.all()
        #if query is not None:
        #blog = blog.filter(

            Q(task__icontains=query) |
            Q(done__icontains=query) 
            )
        context = {
             "tasks_overall": blog,
        } 
        #trick = Tasklist.objects.get(task=entered_name)


        print(f"Found data is {context}")
        print(f"type of context is {type(context)}")'''
        #print(f"type is {type(trick)}")
        #filtered_results['got_data']=trick

        #print(f"FILTERED is {filtered_results}")



        #for i in trick:
            #print(f"Individual element is {i}")

        #print(f" Entered name is {entered_name}")

        #messages.success(request,("New task added!"))

        #print('post req ----->')
        #return HttpResponse('saved')
        return redirect(chintulist)
        #return render(request,'html/filtered.html',context)
        #return render(request,'html/home.html',context)
        #print('post req ----->')
        #return HttpResponse('dat')


    else:
        #return HttpResponse('retry')
        #all_tasks_you_posted = Tasklist.objects.all()
        all_tasks_you_posted = Tasklist.objects.filter(managed_by_user=request.user)
        print(f"all_tasks_found is {all_tasks_you_posted}")
        print(f"type is {type(all_tasks_you_posted)}")
        paginator=Paginator(all_tasks_you_posted,int(8))
        page=request.GET.get('pg')
        all_tasks_you_posted = paginator.get_page(page)
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
@login_required
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
    if task.managed_by_user == request.user:
        task.delete()
    else:
        messages.error(request,("Cannot be deleted by this user"))
        

    return redirect(chintulist)

def editlist(request, task_id):
        if request.method == "POST":
            task=Tasklist.objects.get(pk=task_id)
            form=TaskForm(request.POST or None,instance=task)
            if form.is_valid():
                form.save()
                messages.success(request,("Task edited!"))
            return redirect(chintulist)
            #return HttpResponse('saved data')
        else:
        #return HttpResponse('retry')
            task_object = Tasklist.objects.get(pk=task_id)
            print(f"Task_object is {task_object}")
            #print(f"all_tasks_found is {all_tasks_you_posted}")
            #print(f"type is {type(all_tasks_you_posted)}")

            #print('chintu ana')
            #print(all_tasks_you_posted)
            #print(task_object)

            chintulist_welcome_dict['tasks_overall']=task_object
                #return HttpResponse('chintu called list by him')
                #return render(request,'html/home.html',{})
            return render(request,'html/edit.html',chintulist_welcome_dict)
                #return render(request,'one.html',{})'''
 
            #print('Form is validate')
        '''#data = request.POST.copy()
        #query= data.get('task')
        #blog= Tasklist.objects.all()
        #if query is not None:
        #blog = blog.filter(

            Q(task__icontains=query) |
            Q(done__icontains=query) 
            )
        context = {
             "tasks_overall": blog,
        } 
        #trick = Tasklist.objects.get(task=entered_name)


        print(f"Found data is {context}")
        print(f"type of context is {type(context)}")'''
        #print(f"type is {type(trick)}")
        #filtered_results['got_data']=trick

        #print(f"FILTERED is {filtered_results}")



        #for i in trick:
            #print(f"Individual element is {i}")

        #print(f" Entered name is {entered_name}")

        #messages.success(request,("New task added!"))

        #print('post req ----->')
        #return HttpResponse('saved')
        #return redirect(chintulist)
        #return render(request,'html/filtered.html',context)
        #return render(request,'html/home.html',context)
        #print('post req ----->')
        #return HttpResponse('dat')


def completelist(request,task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.managed_by_user == request.user:
        task.done = True
        task.save()
    
    else:
        messages.error(request,("Cannot be marked as completed!"))

    return redirect(chintulist)

def pendinglist(request,task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.done = False
    task.save()

    return redirect(chintulist)

def indexlist(request):
    contactlist_dict={'cnt_texting':'Index page'}
    #return render(request,'html/about.html',{})
    return render(request,'html/index.html',contactlist_dict)
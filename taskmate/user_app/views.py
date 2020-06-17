from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
from tolist_app import views as tolist_app_views
from user_app.forms import CustomRegisterForm

# Create your views here.

def register(request):
    if request.method == "POST":
        registration_form = CustomRegisterForm(request.POST)
        if registration_form.is_valid():
            #print('correct')
            registration_form.save()
            messages.success(request, ("New user account created ! Login to start"))
        #return redirect(tolist_app_views.chintulist)
        return redirect(register)
        #return render(request,'register.html', {'regform':registration_form})
        #return HttpResponse('Saved')

    #return HttpResponse('Welcome tochintu Registration')
    else:
        registration_form = CustomRegisterForm()
        return render(request,'register.html', {'regform':registration_form})


# Create your views here.

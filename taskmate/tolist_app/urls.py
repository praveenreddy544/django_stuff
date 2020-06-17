from tolist_app import views
from django.urls import path,include

urlpatterns = [
    path('', views.todolist,name='todolist'),
    path('demo',views.demolist,name='dlist'),
    path('home',views.chintulist,name='home_page'),
    #path('contact',views.contactlist,name='contact_page'),
    #path('about',views.aboutlist,name='about_page'),
    path('find',views.chintulist,name='find_page'),
    path('delete/<task_id>',views.deletelist,name='deletetaskid'),
    path('edit/<task_id>',views.editlist,name='edittaskid'),
    path('complete/<task_id>',views.completelist,name='completeid'),
    path('pending/<task_id>',views.pendinglist,name='pendingid'),
]
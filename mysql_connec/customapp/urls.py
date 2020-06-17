from customapp import views
from django.urls import path

urlpatterns = [
    #path('', views.todolist,name='todolist'),
    path('demo',views.demolist,name='dlist'),
    #path('home',views.chintulist,name='home_page'),
    #path('contact',views.contactlist,name='contact_page'),
    #path('about',views.aboutlist,name='about_page')
]
from mydb import views
from django.urls import path

urlpatterns = [
    path('demo',views.demlist,name='dlist'),
    path('ding',views.chklist,name='dlist'),
]
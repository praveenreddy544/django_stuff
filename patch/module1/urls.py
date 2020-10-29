from module1 import views
from django.urls import path

urlpatterns = [
    path('demo',views.demlist,name='dlist'),
    path('ding',views.chklist,name='dlist'),
]
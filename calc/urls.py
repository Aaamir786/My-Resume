from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    
    path('skill',views.skill,name='skill'),

    path('contact',views.contact,name='contact'),

    path('work',views.work,name='work'),
    
     path('hire',views.hire,name='hire'),
    

]

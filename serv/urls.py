from django.urls import path
from . import views

urlpatterns=[
    path('services/',views.services, name='services'),
    path('education/',views.education, name='education'),
    path('personal/',views.personal, name='personal'),
    path('user/',views.user, name='user'),
    


]
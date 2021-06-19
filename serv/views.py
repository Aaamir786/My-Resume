from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here


def services(request):
    context = {'services':'active'}
    return render(request,'services.html',context)

def education(request):
    context = {'education' :'active'}
    return render(request,'education.html',context)

       
    

def personal(request):
    context = {'personal' :'active'}
    return render(request,'personal.html',context)    

def user(request):
    if request.method == 'POST':
        fm = Studentdata(request.POST)
        if fm.is_valid():
            
             name = fm.cleaned_data['name']
             email = fm.cleaned_data['email']
             password = fm.cleaned_data['password']
             password = fm.cleaned_data['rpassword']



             print('name', name)
             print('email', email)
             print('password',password)
             print('Rpassword',password)

             return HttpResponseRedirect('regi/success/')
             #return render(request,'success.html',{'nm':name})   


        # we can used another way to get the data...we can use 'request.POST' instest of "fm.cleaned_data" as..
           #  name = request.POST['name']
           #  email = request.POST['email']
           #  print('name', name)
           #  print('email', email)
         # print( 'cleaned data',fm.cleaned_data)

    else:
       fm = Studentdata()
      

    fm =Studentdata()
    return render(request,'user.html',{'form':fm})   

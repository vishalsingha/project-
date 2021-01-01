from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import  massage_request
from django.http import HttpResponseRedirect
# Create your views here.




def massage(request):
    name = request.POST['Name']
    phone = request.POST['Phone']
    email = request.POST['Email']
    message = request.POST['Message']
    info = massage_request(name= name, email= email, phone= phone, message= message)
    info.save()
    print('info saved')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




def register(request):
    if request.method =='POST':
        first_name = request.POST['First']
        last_name = request.POST['Last']
        username = request.POST['Username']
        email = request.POST['Email']
        password1 = request.POST['Password1']
        password2 = request.POST['Password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username exit..')
                return redirect('/accounts/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already registered...')
                return redirect('/accounts/register')
            else:
                user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, email = email, password = password1)
                user.save()
                print('user created')
                return render(request, 'login.html')
        else:
            messages.info(request,'Password did not match...')
            return redirect('/accounts/register')
        return redirect('/')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('logged in successfully')
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials!!!')
            return redirect('accounts-login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('mainApp:home')
    else:
        if request.method == 'POST':
            form = RegistrationsFrom(request.POST or None)

            if form.is_valid():
                user = form.save()

                raw_password = form.cleaned_data.get('password1')

                user = authenticate(username=user.username,password=raw_password)

                login(request, user)

                return redirect('mainApp:home')
        else:
            form = RegistrationsFrom()
        return render(request, 'acc/register.html',{'form':form})

def loginu(request):
    if request.user.is_authenticated:
        return redirect('mainApp:home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            

            user = authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)               
                    return redirect('mainApp:home')
                else:
                    return render(request, 'acc/login.html', {'error': 'Your Account has been disable.'})
            else:
                return render(request, 'acc/login.html',{'error': 'Invalid username or password. Try again.'})
        return render(request, 'acc/login.html')

def logoutu(request):
    if request.user.is_authenticated:
        logout(request)
        print('Logged out Successfully.')
        return redirect('Accounts:login')
    else:
        return redirect('Accounts:login') 
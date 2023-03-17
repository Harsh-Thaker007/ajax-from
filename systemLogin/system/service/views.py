from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile


# Create your views here.
@login_required(login_url='login')
def Homepage(request):
    return render(request, 'home.html')


def Signuppage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("differ in password")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'signup.html')


def Loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # u = User.objects.get(email=username)
        try:
            print("---")
            u = User.objects.get(email=username)
            print(u)
            user = authenticate(request, username=u.username, password=password)
            new_profile = Profile(username=u.username, password=password)
            new_profile.save()
        except Exception as e:
            print(username)
            user = authenticate(request, username=username, password=password)
            new_profile = Profile(username=username, password=password)
            new_profile.save()

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("username or password incorrect")
    return render(request, 'login.html')


def Logoutpage(request):
    logout(request)
    return redirect('login')

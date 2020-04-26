from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login

# Create your views here.
def home(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if user has right credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
            # A backend authenticated the credentials
        else:
            return render(request, 'login.html') 
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")
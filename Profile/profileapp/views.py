from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .forms import CreateUserForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'profileapp/home.html')

def profile(request):
    return render(request, 'profileapp/profile.html')

def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'{username}, you are logged in.')
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'profileapp/login_page.html')

def register_user(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request,'Account is Created')
            return redirect('login')
        else:
            context = {'form':form}
            messages.info(request, 'Invalid Credentials')
            return render(request, 'profileapp/register_page.html', context)

    context = {'form':form}
    return render(request, 'profileapp/register_page.html', context)

def logout_user(request):
    logout(request)
    messages.info(request, 'you logged out successfully.')
    return redirect('login')

from django.shortcuts import render

# Create your views here.

from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}

    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)

        if ufd.is_valid() and pfd.is_valid():
            MUFDO=ufd.save(commit=False)
            pw=ufd.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()

            MPFDO=pfd.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            send_mail('registration',
            ' Thank you your Registration is scuccessfull',
            'akgupta7440@gmail.com',
            [MUFDO.email],
            fail_silently=False,
            )

            
        else:
            return HttpResponse('Invalid Data')

    return render(request,'registration.html',d)



def home(request):
    if request.session.get('username'):
        
        username=request.session.get('username')
        uo = User.objects.get(username = username)
        d={'username':uo}
        return render(request,'home.html',d)
    return render(request,'home.html')



def user_login(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        AUO=authenticate(username=username,password=password)

        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Invalid Credentials')

    return render(request,'user_login.html')

@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required(login_url='user_login')
def profile_display(request):
    un = request.session.get('username')
    uo = User.objects.get(username = un)
    po = Profile.objects.get(username = uo)
    d = {'uo':uo,'po':po}
    return render(request, 'profile_display.html',d)
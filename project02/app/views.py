from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hey i m in home page")
def template(request):
    return render(request,'index.html')


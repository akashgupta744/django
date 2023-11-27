from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'aksh':['akash','nihal','himanshu']}
    return render(request,'index.html',d)
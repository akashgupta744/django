from django.shortcuts import render

# Create your views here.


def displayfilter(request):
    d= {'data':'hEy heLlo hoW aRe YoU'}
    return render(request,'userfilter.html',d)
    
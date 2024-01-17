from django.shortcuts import render
import datetime
# Create your views here.


def filters(request):
    dt = datetime.datetime.now()
    d = {'data':'akash iS A VeRy GooDBoy', 'dt':dt, 'c':1}
    return render(request, 'filters.html',d)
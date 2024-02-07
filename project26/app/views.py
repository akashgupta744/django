from django.shortcuts import render
from django.views.generic import *
from django.http import HttpResponse
from .forms import*

# Create your views here.

# returning string as response by using fbv
def fbv_string(request):
    return HttpResponse('this is the string from fbv_string')


# returning string as response by using cbv
class CbvString(View):
    def get(self, request):
        return HttpResponse('this is the string from CbvString')


class CbvTemplate(TemplateView):
    template_name = 'CbvTemplate.html'

class CbvForm(FormView):
    
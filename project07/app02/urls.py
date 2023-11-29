from django.urls import path
from app02.views import *

app_name='speciApp02'
urlpatterns=[
    path('akash/',akash,name='akash'),
]
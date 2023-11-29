from django.urls import path
from app01.views import *

app_name='speciApp01'
urlpatterns=[
    path('akash/',akash,name='akash'),
]
 
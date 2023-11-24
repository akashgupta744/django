from django.urls import path
from app2.views import *

urls_name="specific"

urlpatterns=[
    path('specific/',specific,name='specific')
]
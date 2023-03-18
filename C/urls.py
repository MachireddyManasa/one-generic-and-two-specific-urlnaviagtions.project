from django.urls import path
from C.views import *
app_name='C'
urlpatterns=[
    path('five/',five,name='five'),
    path('six/',six,name='six'),
]
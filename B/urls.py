from django.urls import path
from B.views import *
app_name='B'
urlpatterns=[
    path('three/',three,name='three'),
    path('four/',four,name='four'),
]
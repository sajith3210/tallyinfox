from django.urls import path
from tallyapp import views

urlpatterns = [

    path('',views.index,name='index'),
    path('stockgroup/',views.stockgroup,name='stockgroup'),
]
from django.urls import path
from tallyapp import views

urlpatterns = [

    path('',views.index,name='index'),
    path('stockgroup/',views.stockgroup,name='stockgroup'),
    path('stockcategory/',views.stockcategory,name='stockcategory'),
    path('stockitem/',views.stockitem,name='stockitem'),
    path('unitalteration/',views.unitalter,name='unitalteration'),
    path('locationalteration/',views.locationalter,name='locationalteration'),
    path('companypricelevel/',views.companypricelevel,name='companypricelevel'),
    path('liststockgroup/',views.liststockgroup,name='liststockgroup'),
    path('stockgroupalter/<int:pk>/',views.stockgroupalter,name='stockgroupalter'),
    path('stockgroupdelete/<int:pk>/',views.stockgroupdelete,name='stockgroupdelete'),
    path('stockcategoryalter/<int:pk>/',views.stockcategoryalter,name='stockcategoryalter'),
]
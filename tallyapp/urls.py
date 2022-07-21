from unicodedata import name
from django.urls import path
from tallyapp import views

urlpatterns = [

    path('',views.index,name='index'),
    path('stockgroup/',views.stockgroup,name='stockgroup'),
    path('stockcategory/',views.stockcategory,name='stockcategory'),
    path('stockitem/',views.stockitem,name='stockitem'),
    path('unitalteration/',views.unitalter,name='unitalteration'),
    
    path('companypricelevel/',views.companyprice_level,name='companypricelevel'),

    path('liststockgroup/',views.liststockgroup,name='liststockgroup'),
    path('stockgroupalter/<int:pk>/',views.stockgroupalter,name='stockgroupalter'),
    path('stockgroupdelete/<int:pk>/',views.stockgroupdelete,name='stockgroupdelete'),

    path('listofstockcategories/',views.listofstockcategories,name='listofstockcategories'),
    path('stockcategoryalter/<int:pk>/',views.stockcategoryalter,name='stockcategoryalter'),
    path('stockcategorydelete/<int:pk>/',views.stockcategorydelete,name='stockcategorydelete'),

    path('locationcreation/',views.locationcreation,name='locationcreation'),
    path('listoflocation/',views.listoflocation,name='listoflocation'),
    path('locationalteration/<int:pk>/',views.locationalter,name='locationalteration'),
    path('locationdelete/<int:pk>/',views.locationdelete,name='locationdelete'),

    path('simpleunit/',views.simpleunit,name='simpleunit'),
    path('compoundunit/',views.compoundunit,name='compoundunit'),
]
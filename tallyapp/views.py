from tkinter import messagebox
from django.shortcuts import redirect, render
from  tallyapp.models import *
from django.contrib import messages
# Create your views here.
def index(request):

    return render(request,'index.html')

def stockgroup(request):
    stock_grou=stock_group.objects.all()
    if request.method=="POST":
        nme=request.POST['stock_group_name'].title()
        alia=request.POST['stock_group_alias']
        und=request.POST['stock_group_under']
        should_quantity_item=request.POST['quantity_item']

        if stock_group.objects.filter(stock_group_name=nme).exists():
            messages.info(request,'Name already exists Enter a diffrent name')
            return redirect('stockgroup')
        else:   
            su=stock_group(stock_group_name=nme,alias=alia,under=und,should_quantity_of_items_be_added=should_quantity_item) 
            su.save() 
            messages.info(request,'Stock group save successfully') 
            return redirect('stockgroup')
    return render(request,'stock group creation.html',{'st':stock_grou})

def liststockgroup(request):
    stock_grou=stock_group.objects.all()
    return render(request,'list of stock groups.html',{'st':stock_grou})
    


def stockgroupalter(request,pk):
    stock_one_object=stock_group.objects.get(id=pk) #Fetch value one object
    stock_grou=stock_group.objects.all() #Feth value for drop down control
    if request.method=="POST":
        stktable=stock_group.objects.get(id=pk)
        stktable.stock_group_name=request.POST['stock_group_name'].title()
        stktable.alias=request.POST['stock_group_alias']
        stktable.under=request.POST['stock_group_under']
        stktable.should_quantity_of_items_be_added=request.POST['quantity_item']
        stktable.save()
        return redirect('liststockgroup')
        # if stock_group.objects.filter(stock_group_name=nme).exists():
        #     messages.info(request,'Name already exists Enter a diffrent name')
        #     return redirect('stockgroupalter')
        # else:   
        #     su=stock_group(stock_group_name=nme,alias=alia,under=und,should_quantity_of_items_be_added=should_quantity_item) 
        #     su.save() 
        #     messages.info(request,'Stock group alter successfully') 
        #     return redirect('stockgroupalter')   
    return render(request,'stockgroupalter.html',{'st':stock_grou,'st_one':stock_one_object})
    
def stockgroupdelete(request,pk):
    stktable=stock_group.objects.get(id=pk)   
    stktable.delete()
    return redirect('liststockgroup')

def stockcategory(request):
    stcat=stock_category.objects.all()
    if request.method=="POST":
        ctname=request.POST['catname']
        ctalias=request.POST['catalias']
        ctunder=request.POST['catunder']
        if stock_category.objects.filter(stock_category_name=ctname).exists():
            messages.info(request,'Stock category name already exists')
        else:
            st=stock_category(stock_category_name=ctname,alias=ctalias,under=ctunder)
            st.save()
            messages.info(request,'Stock category save successfully')
    return render(request,'stock category creation.html',{'st':stcat})

def listofstockcategories(request):
    stcat=stock_category.objects.all()
    return render(request,'list of stock categories.html',{'st':stcat})

def stockcategoryalter(request):
    pass

def stockitem(request):
    return render(request,'stock item creation.html')

def unitalter(request):
    return render(request,'unit alteration.html')

def locationalter(request):
    return render(request,'Location alteration.html')

def companypricelevel(request):
    return render(request,'company price level.html')

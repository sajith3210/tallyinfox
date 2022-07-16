from django.shortcuts import render
from  tallyapp.models import *
# Create your views here.
def index(request):

    return render(request,'index.html')

def stockgroup(request):
    stock_grou=stock_group.objects.all()
    if request.method=="POST":
        nme=request.POST['stock_group_name']
        alia=request.POST['stock_group_alias']
        und=request.POST['stock_group_under']
        should_quantity_item=request.POST['quantity_item']

        if stock_grou.objects.get(stock_group_name=nme).exists():
            
        su=stock_group(stock_group_name=nme,alias=alia,under=und,should_quantity_of_items_be_added=should_quantity_item) 
        su.save()  
    return render(request,'stock group creation.html',{'st':stock_grou})

def stockcategory(request):
    return render(request,'stock category creation.html')

def stockitem(request):
    return render(request,'stock item creation.html')

def unitalter(request):
    return render(request,'unit alteration.html')

def locationalter(request):
    return render(request,'Location alteration.html')

def companypricelevel(request):
    return render(request,'company price level.html')
